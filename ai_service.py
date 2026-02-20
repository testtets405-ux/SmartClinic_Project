"""
================================================================================
محرك الذكاء الاصطناعي الخاص بالعيادة (ai_service.py)
================================================================================
الهدف المنهجي (للطالب):
في العالم الحقيقي، وقت الانتظار للمريض ليس ثابتاً (ليس دائماً 15 دقيقة لكل مريض).
بل يتأثر بعوامل متغيرة عديدة:
1. طول طابور الانتظار (queue_length) لحظة دخول المريض.
2. توقيت الزيارة (hour_of_day) (هل هي ساعة ذروة مثل 1 ظهراً، أم وقت هادئ؟).
3. أيام الأسبوع (day_of_week) (هل هو يوم عطلة مزدحم أم منتصف الأسبوع؟).
4. نوع الكشف (appointment_type_encoded) (الطوارئ تعطّل الطابور، الكشف الجديد يحتاج وقتاً أطول).

هذا الملف يحتوي على خوارزمية التعلم الآلي البارزة الغابات العشوائية (RandomForestRegressor) 
من مكتبة (scikit-learn) والتي تقوم ببناء نموذج رياضي ذكي يتعلم من سلوك العيادة 
السابق (بيانات تاريخية) ليتوقع وقت الانتظار الدقيق للمريض الجديد!

إذا واجه النظام نقصاً في البيانات الحقيقية بالداتا بيس (أقل من 10 مرضى مسجلين)، يقوم 
تلقائياً بتوليد (بيانات اصطناعية - Synthetic Data) ليدرب نفسه عليها لضمان عدم 
انهيار وعدم توقف الخدمة عن العمل (Fallback Mechanism).
================================================================================
"""

import random
from datetime import datetime

# --- Try importing scikit-learn ---
try:
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import LabelEncoder
    import numpy as np
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

# Map appointment types to numeric codes
APPT_TYPE_MAP = {"emergency": 2, "follow_up": 1, "checkup": 0}


class WaitTimePredictor:
    """
    محرك ذكاء اصطناعي حقيقي لتوقع وقت الانتظار.

    الميزات المستخدمة في التنبؤ:
    - queue_len: عدد المرضى في قائمة الانتظار
    - hour:      ساعة الزيارة الحالية
    - day:       يوم الأسبوع (0=الاثنين، 6=الأحد)
    - appt_type: نوع الموعد (0=كشف، 1=متابعة، 2=طوارئ)
    """

    def __init__(self):
        self.model = None
        self.is_trained = False
        self.training_source = "none"

        # حقول الأوزان الاحتياطية (تُستخدم إذا لم يكن sklearn متوفراً)
        self.weights = {
            "base_per_patient": 15.0,
            "peak_hour_factor": 1.3,
            "weekend_factor": 1.15,
        }

    def _generate_synthetic_samples(self, n=800):
        """توليد بيانات تاريخية اصطناعية للتدريب الشامل."""
        samples_X, samples_y = [], []
        for _ in range(n):
            queue_len = random.randint(0, 20)
            hour = random.randint(8, 22)
            day = random.randint(0, 6)
            appt_type = random.choice([0, 1, 2])

            base = 12.0
            peak = 1.3 if 10 <= hour <= 14 else 1.0
            weekend = 1.15 if day >= 4 else 1.0
            urgency = 0.7 if appt_type == 2 else (1.1 if appt_type == 0 else 1.0)

            minutes = (queue_len + 1) * base * peak * weekend * urgency
            minutes *= random.uniform(0.98, 1.02)  # ±2% تقليل التشويش لنتائج منطقية ومستقرة

            samples_X.append([queue_len, hour, day, appt_type])
            samples_y.append(minutes)
        return samples_X, samples_y

    def train(self, patients=None):
        """
        تدريب النموذج على بيانات حقيقية من DB أو بيانات اصطناعية كاحتياط.
        يُستدعى عند بدء التطبيق.
        """
        if not SKLEARN_AVAILABLE:
            print("AI Engine: scikit-learn غير متوفر، يتم استخدام النموذج الاحتياطي.")
            self._train_fallback()
            return

        real_X, real_y = [], []

        # محاولة استخدام بيانات حقيقية من قاعدة البيانات
        if patients and len(patients) >= 10:
            now = datetime.now()
            for p in patients:
                try:
                    hour = p.check_in_time.hour if p.check_in_time else now.hour
                    day = p.check_in_time.weekday() if p.check_in_time else now.weekday()
                    appt_enc = APPT_TYPE_MAP.get(p.appointment_type, 0)
                    # وقت الانتظار الفعلي (بالدقائق) — إذا توفر من السجل
                    if hasattr(p, 'wait_minutes') and p.wait_minutes is not None:
                        real_X.append([0, hour, day, appt_enc])
                        real_y.append(float(p.wait_minutes))
                except Exception:
                    continue

        if len(real_X) >= 10:
            X_train, y_train = real_X, real_y
            self.training_source = "database"
            print(f"AI Engine: تدريب على {len(X_train)} سجل حقيقي من قاعدة البيانات.")
        else:
            # بيانات DB غير كافية — استخدام بيانات اصطناعية
            X_train, y_train = self._generate_synthetic_samples(800)
            self.training_source = "synthetic"
            print("AI Engine: تدريب على بيانات اصطناعية (قاعدة البيانات فارغة أو صغيرة).")

        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=8,
            random_state=42,
            n_jobs=-1
        )
        self.model.fit(np.array(X_train), np.array(y_train))
        self.is_trained = True
        print(f"AI Engine: تم التدريب بنجاح | المصدر: {self.training_source}")

    def _train_fallback(self):
        """نموذج احتياطي خطي بدون scikit-learn."""
        X, y = self._generate_synthetic_samples(500)
        per_patient = [yi / (xi[0] + 1) for xi, yi in zip(X, y)]
        self.weights["base_per_patient"] = sum(per_patient) / len(per_patient)
        self.is_trained = True
        self.training_source = "fallback"
        print("AI Engine: تم ضبط النموذج الاحتياطي.")

    def predict(self, queue_len: int, appointment_type: str = "checkup") -> int:
        """
        توقع وقت الانتظار بالدقائق.

        المدخلات:
        - queue_len:       عدد المرضى في الطابور
        - appointment_type: نوع الموعد (emergency/follow_up/checkup)
        """
        if not self.is_trained:
            self.train()

        now = datetime.now()
        hour = now.hour
        day = now.weekday()
        appt_enc = APPT_TYPE_MAP.get(appointment_type, 0)

        if SKLEARN_AVAILABLE and self.model is not None:
            import numpy as np
            features = np.array([[queue_len, hour, day, appt_enc]])
            pred = self.model.predict(features)[0]
            # بدون تشويش عشوائي — النتيجة حتمية ودقيقة (Deterministic)
            return max(1, int(pred))
        else:
            # النموذج الاحتياطي
            est = (queue_len + 1) * self.weights["base_per_patient"]
            if 10 <= hour <= 14:
                est *= self.weights["peak_hour_factor"]
            if day >= 4:
                est *= self.weights["weekend_factor"]
            # بدون تشويش — حتمي ومستقر
            return max(1, int(est))

    def get_status(self) -> dict:
        """إرجاع معلومات حالة المحرك للواجهة."""
        return {
            "trained": self.is_trained,
            "source": self.training_source,
            "sklearn": SKLEARN_AVAILABLE,
            "model_type": "RandomForestRegressor" if SKLEARN_AVAILABLE else "LinearFallback"
        }


# Singleton instance
ai_engine = WaitTimePredictor()
