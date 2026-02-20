"""
================================================================================
نماذج وهندسة قاعدة البيانات (models.py)
================================================================================
الهدف المنهجي (للطالب):
في تطبيقات الفلاسك الحديثة، كتابة استعلامات SQL يدوياً عُرضة لثغرات الـ (SQL Injection). 
لذلك نستخدم مكتبة (SQLAlchemy ORM)، وفيها يتم تحويل كل "جدول - Table" في قاعدة 
البيانات إلى "كائن بايثون - Class"، وكل "عمود - Column" إلى "متغير - Attribute".

هذا الملف الطويل هو خريطتك الهيكلية ويتكون من 3 جداول أساسية:
1. جدول (User): يحوي حسابات الدخول المشفرة لموظفي النظام باختلاف أدوارهم (صلاحياتهم).
2. جدول (Patient): يحوي حالة المريض ونقاطه أثناء دورة حياته بالعيادة (منتظر، بالعيادة، انتهى).
3. جدول (Appointment): هذا هو "الجدول الرابط (Relation)" الذي يربط بين جدول الطبيب 
   وجدول المريض، ويوثق التشخيص والتاريخ بمجرد خروج المريض من الغرفة لضمان تاريخ طبي سليم للاستعراض.
================================================================================
"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# ── كائن قاعدة البيانات — يُهيَّأ مع التطبيق في app.py ──
db = SQLAlchemy()


class User(UserMixin, db.Model):
    """
    جدول المستخدمين (users) — يمثل موظفي النظام.

    الأدوار المتاحة:
      - admin       → مسؤول كامل الصلاحيات
      - doctor      → طبيب (يرى لوحة الكشف)
      - receptionist → موظف استقبال (يرى لوحة الاستقبال)

    يرث من UserMixin ليدعم Flask-Login تلقائياً.
    كلمة المرور تُخزن كـ Hash فقط، ولا تُخزن بنص صريح أبداً.
    """
    __tablename__ = "users"

    # ── المعرف الفريد لكل مستخدم ──
    id = db.Column(db.Integer, primary_key=True)

    # ── اسم المستخدم (فريد — يُستخدم لتسجيل الدخول) ──
    username = db.Column(db.String(80), unique=True, nullable=False)

    # ── Hash كلمة المرور (لا تُقرأ بنص صريح أبداً) ──
    password_hash = db.Column(db.String(256), nullable=False)

    # ── الدور: admin | doctor | receptionist ──
    role = db.Column(db.String(20), nullable=False, default="doctor")

    def set_password(self, password: str):
        """
        تشفير كلمة المرور وحفظها.

        يستخدم Werkzeug لتوليد Hash آمن (PBKDF2-SHA256).
        يُستدعى عند إنشاء أو تغيير كلمة المرور.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        مقارنة كلمة المرور المدخلة مع الـ Hash المخزن.

        تُعيد True إذا كانت كلمة المرور صحيحة، وFalse خلاف ذلك.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username} ({self.role})>"


class Patient(db.Model):
    """
    جدول المرضى (patients) — يمثل زيارة مريض واحدة.

    دورة حياة المريض في النظام:
      waiting → in_progress → done

    التدفق:
      1. المريض يسجل في Kiosk أو الاستقبال → status=waiting
      2. الطبيب يستدعيه → status=in_progress
      3. الطبيب ينهي الكشف → status=done + يُنشأ appointment

    القيم المقبولة في الحقول:
      appointment_type: checkup | follow_up | emergency
      status:           waiting | in_progress | done
      gender:           male | female
    """
    __tablename__ = "patients"

    # ── المعرف الفريد ──
    id = db.Column(db.Integer, primary_key=True)

    # ── الاسم الكامل للمريض ──
    name = db.Column(db.String(120), nullable=False)

    # ── العمر بالسنوات (يؤثر على حساب الأولوية) ──
    age = db.Column(db.Integer, nullable=False)

    # ── الجنس: male | female ──
    gender = db.Column(db.String(10), nullable=False)

    # ── نوع الزيارة: checkup | follow_up | emergency ──
    # يحدد الطبقة في نظام الأولوية ثنائي المستوى
    appointment_type = db.Column(db.String(20), nullable=False, default="checkup")

    # ── الحالة الحالية في تدفق العمل ──
    # waiting=في الانتظار | in_progress=بالعيادة | done=انتهى
    status = db.Column(db.String(20), nullable=False, default="waiting")

    # ── درجة الأولوية المحسوبة (AgeBonusScore + WaitFactor) ──
    # أعلى نقطة = يُخدَم أولاً ضمن طبقته
    priority_score = db.Column(db.Integer, nullable=False, default=0)

    # ── وقت الحضور — يُخزن UTC دائماً، يُعرض بوقت بغداد ──
    check_in_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Patient {self.name} score={self.priority_score}>"


class Appointment(db.Model):
    """
    جدول سجلات الكشف (appointments) — يربط المريض بالطبيب مع التشخيص.

    يُنشأ سجل جديد عندما:
      - الطبيب ينهي الكشف وكتب تشخيصاً
      - أو عند seed البيانات لإنشاء سجل تاريخي

    الحقول:
      patient_id     → معرف المريض (Foreign Key → patients.id)
      doctor_id      → معرف الطبيب  (Foreign Key → users.id, قد يكون None)
      scheduled_time → وقت إجراء الكشف (UTC)
      notes          → نص التشخيص أو ملاحظات الطبيب
    """
    __tablename__ = "appointments"

    # ── المعرف الفريد للسجل ──
    id = db.Column(db.Integer, primary_key=True)

    # ── معرف المريض (مرتبط بجدول patients) ──
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)

    # ── معرف الطبيب (مرتبط بجدول users، قد يكون فارغاً) ──
    doctor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    # ── وقت الكشف — UTC ──
    scheduled_time = db.Column(db.DateTime, nullable=True)

    # ── نص التشخيص أو ملاحظات الطبيب ──
    notes = db.Column(db.Text, nullable=True)

    # ── العلاقات (Relationships) للوصول السهل ──
    # appointment.patient.name → اسم المريض
    patient = db.relationship("Patient", backref="appointments")
    # appointment.doctor.username → اسم المستخدم الطبيب
    doctor = db.relationship("User", backref="appointments")

    def __repr__(self):
        return f"<Appointment patient_id={self.patient_id}>"
