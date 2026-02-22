"""
================================================================================
سكربت تهيئة وزرع البيانات (seed_db.py)
================================================================================
الهدف المنهجي (للطالب):
عند برمجة وتطوير النظام، نحتاج دائماً لبيانات وهمية لتجربة شكل الجداول والإحصائيات وتدريب 
محرك الذكاء الاصطناعي (Machine Learning). من المتعب إدخال 50 مريضاً يدوياً كل مرة!
لذا، هذا السكربت العظيم يقوم بالتالي بضغطة زر (python seed_db.py):
1. يمسح قاعدة البيانات القديمة بالكامل ويُنشئ واحدة جديدة نظيفة تماماً.
2. يُنشئ حسابات الموظفين (admin, doctor, reception) بكلمة مرور 123 للراحة أثناء التطوير.
3. يقوم بتوليد مرضى وهميين (طوارئ، أطفال، شيوخ) بأوقات حضور مُتفاوتة في الماضي، 
   لمحاكاة طابور انتظار حقيقي ومزدحم.
4. يولد سجلات تاريخية لكشوفات سابقة مع تشخيصات طبية واقعية لإثراء لوحة الإحصائيات.

[تعليمات وتحذير مهم جداً]:
استخدم هذا الملف فقط في بيئة التطوير (Development) لغرض التجربة، أو عند الرفع لأول مرة.
لا تقم بتشغيله أبداً في الإنتاج الفعلي (Production) لاحقاً لأنه سيمسح بيانات المرضى الحقيقيين بالكامل!
================================================================================
"""

import sys
import os
import random
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from models import db, User, Patient, Appointment
from utils import calculate_priority


def seed():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("✔ تم تهيئة قاعدة البيانات من جديد.")

        # ─── إنشاء المستخدمين ───
        admin = User(username="admin", role="admin")
        admin.set_password("123")
        doctor = User(username="doctor", role="doctor")
        doctor.set_password("123")
        receptionist = User(username="reception", role="receptionist")
        receptionist.set_password("123")
        db.session.add_all([admin, doctor, receptionist])
        db.session.commit()
        print("✔ تم إنشاء المستخدمين: admin/123, doctor/123, reception/123")

        now = datetime.now(timezone.utc)  # UTC دائماً

        diagnoses = [
            "نزلة برد حادة مع وصف خافض حرارة",
            "ارتفاع ضغط الدم يحتاج متابعة شهرية",
            "سكري من النوع الثاني — تنظيم جرعات الإنسولين",
            "آلام معدة نتيجة التهاب بسيط",
            "التهاب حلق فيروسي مع راحة وسوائل",
            "حساسية صدرية موسمية بالجهاز التنفسي",
            "متابعة ما بعد عملية جراحية بسيطة",
            "فقر دم خفيف مع وصف مكملات حديد",
            "صداع نصفي مزمن — مراجعة خطة العلاج",
            "آلام أسفل الظهر مع إحالة للعلاج الطبيعي",
            "قصة تاريخية: التهاب مفاصل — وصف مضاد التهاب",
            "متابعة قصور الغدة الدرقية — تحليل TSH",
            "طارئ: أزمة ربو حادة — مضادات حيوية + بخاخ",
            "طارئ: كسر في الرسغ — تحويل إلى الجراحة",
        ]

        # ─── بيانات الأسماء ───
        male_names   = ["محمد", "أحمد", "محمود", "يوسف", "علي", "عمر", "إبراهيم",
                        "خالد", "حسن", "حسين", "طارق", "ياسر", "سامر", "وسيم"]
        female_names = ["سارة", "فاطمة", "مريم", "نور", "ليلى", "هنا", "سلمى",
                        "آية", "زينب", "هدى", "رهام", "تسنيم", "شروق", "لنا"]
        last_names   = ["علي", "محمد", "حسن", "إبراهيم", "محمود", "سعيد",
                        "مصطفى", "عبدالله", "عثمان", "صالح", "نوري", "عمر"]

        def rand_name():
            is_m = random.choice([True, False])
            fn   = random.choice(male_names if is_m else female_names)
            ln   = random.choice(last_names)
            return f"{fn} {ln}", "male" if is_m else "female"

        def rand_age(category="mixed"):
            if category == "child":   return random.randint(1,  12)
            if category == "young":   return random.randint(18, 40)
            if category == "adult":   return random.randint(41, 59)
            if category == "elderly": return random.randint(60, 90)
            return random.choices(
                [random.randint(1,12), random.randint(13,17),
                 random.randint(18,55), random.randint(56,90)],
                weights=[15, 10, 50, 25]
            )[0]

        patients = []
        appointments = []

        # ════════════════════════════════════════════════════
        # 1. مرضى منتهون (done) — جاؤوا في بداية اليوم
        # ════════════════════════════════════════════════════
        done_scenarios = [
            # (type,         age_cat,   minutes_ago_range)
            ("emergency",    "elderly",  (180, 300)),
            ("follow_up",    "adult",    (150, 240)),
            ("checkup",      "young",    (120, 200)),
            ("follow_up",    "elderly",  (110, 180)),
            ("checkup",      "child",    (100, 170)),
            ("checkup",      "young",    (90,  160)),
            ("follow_up",    "adult",    (80,  150)),
            ("emergency",    "adult",    (75,  140)),
            ("checkup",      "elderly",  (70,  130)),
            ("follow_up",    "young",    (60,  120)),
        ]
        for appt_type, age_cat, (lo, hi) in done_scenarios:
            name, gender = rand_name()
            age = rand_age(age_cat)
            minutes_ago = random.randint(lo, hi)
            check_in = now - timedelta(minutes=minutes_ago)
            score = calculate_priority(age, appt_type, 0)
            p = Patient(name=name, age=age, gender=gender,
                        appointment_type=appt_type, status="done",
                        priority_score=score, check_in_time=check_in)
            patients.append(p)

        # ════════════════════════════════════════════════════
        # 2. المريض قيد الكشف (1 فقط)
        # ════════════════════════════════════════════════════
        name, gender = rand_name()
        age = rand_age("adult")
        in_prog = Patient(
            name=name, age=age, gender=gender,
            appointment_type="follow_up", status="in_progress",
            priority_score=calculate_priority(age, "follow_up", 0),
            check_in_time=now - timedelta(minutes=random.randint(15, 30)),
        )
        patients.append(in_prog)

        # ════════════════════════════════════════════════════
        # 3. مرضى الانتظار — سيناريوهات حقيقية متنوعة
        # ════════════════════════════════════════════════════
        waiting_scenarios = [
            # (type,         age_cat,   minutes_ago)  ← كلما أكبر = انتظر أطول
            ("emergency",    "elderly",  55),   # طوارئ شيخ → أعلى أولوية
            ("emergency",    "child",    30),   # طوارئ طفل → أولوية 2
            ("follow_up",    "elderly",  85),   # كبير سن انتظر طويلاً
            ("follow_up",    "elderly",  60),   # كبير سن
            ("follow_up",    "adult",    75),   # بالغ انتظر 75 دقيقة
            ("follow_up",    "adult",    50),   # بالغ انتظر 50 دقيقة
            ("follow_up",    "young",    65),   # شاب انتظر 65 دقيقة
            ("follow_up",    "young",    40),   # شاب انتظر 40 دقيقة
            ("checkup",      "child",    45),   # طفل كشف عادي
            ("checkup",      "young",    35),   # شاب كشف عادي
            ("checkup",      "adult",    25),   # بالغ كشف عادي
            ("checkup",      "elderly",  20),   # كبير سن وصل حديثاً
            ("checkup",      "young",    10),   # شاب وصل حديثاً
            ("checkup",      "adult",    5),    # بالغ وصل للتو
        ]
        for appt_type, age_cat, minutes_ago in waiting_scenarios:
            name, gender = rand_name()
            age = rand_age(age_cat)
            check_in = now - timedelta(minutes=minutes_ago)
            score = calculate_priority(age, appt_type, minutes_ago)
            p = Patient(name=name, age=age, gender=gender,
                        appointment_type=appt_type, status="waiting",
                        priority_score=score, check_in_time=check_in)
            patients.append(p)

        db.session.add_all(patients)
        db.session.commit()

        # ─── سجلات الزيارات التاريخية ───
        done_and_current = [p for p in Patient.query.all()
                            if p.status in ("done", "in_progress")]
        for patient in done_and_current:
            for _ in range(random.randint(1, 3)):
                days_ago = random.randint(7, 365)
                visit_time = now - timedelta(days=days_ago,
                                             hours=random.randint(0, 4))
                appointments.append(Appointment(
                    patient_id=patient.id, doctor_id=doctor.id,
                    scheduled_time=visit_time,
                    notes=random.choice(diagnoses),
                ))
        db.session.add_all(appointments)
        db.session.commit()

        # ─── ملخص ───
        total = Patient.query.count()
        w = Patient.query.filter_by(status="waiting").count()
        ip = Patient.query.filter_by(status="in_progress").count()
        d = Patient.query.filter_by(status="done").count()
        em = Patient.query.filter_by(appointment_type="emergency").count()
        print("=" * 50)
        print("         ملخص سكربت التهيئة")
        print("=" * 50)
        print(f"  المرضى الكلي        : {total}")
        print(f"  - في الانتظار       : {w}  (منهم {em} طوارئ)")
        print(f"  - قيد الكشف     (1) : {ip}")
        print(f"  - تم الكشف          : {d}")
        print(f"  سجلات الزيارات      : {len(appointments)}")
        print("=" * 50)
        print("  بيانات الدخول:")
        print("    أدمن    → admin / 123")
        print("    طبيب    → doctor / 123")
        print("    استقبال → reception / 123")
        print("=" * 50)
        print("\n  سيناريوهات الانتظار النشطة:")
        waiting_patients = Patient.query.filter_by(status="waiting").all()
        for p in sorted(waiting_patients, key=lambda x: -x.priority_score):
            tier = "🔴 طوارئ" if p.appointment_type == "emergency" else (
                   "🟡 متابعة" if p.appointment_type == "follow_up" else "🟢 كشف")
            print(f"  [{tier}] {p.name} | عمر {p.age} | {p.priority_score} نقطة")


if __name__ == "__main__":
    seed()
