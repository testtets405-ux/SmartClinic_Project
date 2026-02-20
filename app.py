"""
================================================================================
الملف الرئيسي للتطبيق (app.py) - قلب المشروع
================================================================================
الهدف المنهجي (للطالب):
هذا هو الملف المركزي (Entry Point) الذي يعتمد عليه إطار عمل (Flask - فلاسك).
وظيفته الأساسية هي تعريف "الروابط والمنافذ - Routes" التي يدخل عليها المستخدم من المتصفح،
وربطها بالدوال التي تنفذ العمليات في الخلفية وتُعيد قوالب HTML المناسبة (Templates).

أقسام الملف الهندسية:
1. [التهيئة - App Factory]: دالة (create_app) التي تربط قاعدة البيانات ونظام الحماية.
2. [المسارات المفتوحة - Public Routes]: روابط لا تحتاج تسجيل دخول (شاشة Kiosk وشاشة Queue).
3. [المسارات المحمية - Protected Routes]: محمية بنظام (login_required) وتتوزع بين:
   - الاستقبال (Reception): لإدخال المرضى وإدارة وصولهم.
   - الطبيب (Doctor): يرى المريض الحالي، ينهي الكشف، ويكتب التشخيص.
   - الإدارة (Admin): لوحة التحكم الشاملة لإنشاء المستخدمين ومتابعة الإحصائيات.
4. [واجهة برمجة التطبيقات - APIs]: مسارات لا تُعيد صفحات HTML بل بيانات نصية مضغوطة 
   بصيغة (JSON)، وتستخدمها الجافاسكريبت لتحديث الرسومات والطابور بصورة حية خلف الكواليس!
================================================================================
"""

import sys
import os

# ── [إصلاح بيئة الاستضافة]: التصريح بمسار الحزم المثبتة بواسطة المستخدم (user-site) ──
# يفيد هذا الكود في بيئات مثل PythonAnywhere حيث تُثبت مكتبات مثل scikit-learn في 
# مجلد المستخدم وليس في جذور النظام.
_user_sp = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Python')
for _root, _dirs, _ in os.walk(_user_sp):
    for _d in _dirs:
        if _d == 'site-packages':
            _sp_path = os.path.join(_root, _d)
            if _sp_path not in sys.path:
                sys.path.insert(0, _sp_path)
    break  # only top-level sub-dirs

from datetime import datetime, timezone
from functools import wraps
from io import StringIO
import csv

from clock import now_utc, to_local, fmt_local, wait_duration_str

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
    make_response,
)
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)

from config import Config
from models import db, User, Patient, Appointment
from utils import calculate_priority, estimate_wait_time, get_urgency_tier
from ai_service import ai_engine

login_manager = LoginManager()
login_manager.login_message = "يرجى تسجيل الدخول للوصول إلى هذه الصفحة."
login_manager.login_message_category = "warning"


def update_queue_priorities():
    """
    تحديث أولويات الانتظار بناءً على وقت الانتظار الحالي.
    يتم استدعاء هذه الدالة دورياً لضمان زيادة النقاط مع مرور الوقت.
    """
    try:
        waiting_patients = Patient.query.filter_by(status="waiting").all()
        now = now_utc()
        for p in waiting_patients:
            p_time = p.check_in_time
            if p_time.tzinfo is None:
                p_time = p_time.replace(tzinfo=timezone.utc)
                
            wait_duration = now - p_time
            waiting_minutes = int(wait_duration.total_seconds() / 60)
            
            if waiting_minutes < 0:
                waiting_minutes = 0
                
            # إعادة حساب الأولوية مع عامل الوقت
            new_score = calculate_priority(p.age, p.appointment_type, waiting_minutes)
            if p.priority_score != new_score:
                p.priority_score = new_score
        
        db.session.commit()
    except Exception as e:
        print(f"Error updating priorities: {e}")
        db.session.rollback()


def role_required(*roles):
    """
    ديكوريتور عام لاشتراط وجود دور (Role) معيّن للدخول على الراوت.
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                flash("ليست لديك صلاحية الوصول إلى هذه الصفحة.", "danger")
                return redirect(url_for("home"))
            return view_func(*args, **kwargs)
        return wrapped
    return decorator

def create_app() -> Flask:
    """
    دالة المصنع (Factory) لإنشاء وتهيئة تطبيق Flask.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    # تسجيل فلتر توقيت بغداد ليكون متاحاً في كل القوالب (clinic_time)
    @app.template_filter("iraqtime")
    def iraq_time_filter(dt, fmt="%I:%M %p"):
        return fmt_local(dt, fmt)

    with app.app_context():
        db.create_all()
        # Initial AI Engine training on real DB data
        try:
            patients = Patient.query.all()
            ai_engine.train(patients=patients)
        except Exception as e:
            print(f"AI Engine Init Failed: {e}")
            ai_engine.train()  # fallback to synthetic

    register_routes(app)
    return app

@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))

def register_routes(app: Flask):
    """
    دالة تجمع وتعرّف جميع المسارات الخاصة بالتطبيق.
    """
    # ---------- Home ----------
    @app.route("/")
    def home():
        return render_template("index.html")

    # ---------- Kiosk (Patient Check-in, Public) ----------
    @app.route("/kiosk", methods=["GET", "POST"])
    def kiosk():
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            age = request.form.get("age", type=int)
            gender = request.form.get("gender", "male")
            appointment_type = request.form.get("appointment_type", "checkup")

            if not name or age is None:
                flash("يرجى ملء جميع الحقول المطلوبة.", "danger")
                return redirect(url_for("kiosk"))

            check_in = now_utc()  # تخزين UTC دائماً — يعرض بتوقيت بغداد عبر الفلتر
            score = calculate_priority(age, appointment_type)

            patient = Patient(
                name=name,
                age=age,
                gender=gender,
                appointment_type=appointment_type,
                status="waiting",
                priority_score=score,
                check_in_time=check_in,
            )
            db.session.add(patient)
            db.session.commit()
            flash("تم تسجيل دخولك لقائمة الانتظار. سيتم استدعاؤك عند حلول دورك.", "success")
            return redirect(url_for("kiosk"))

        waiting_count = Patient.query.filter_by(status="waiting").count()
        wait_minutes = ai_engine.predict(waiting_count)
        hours = wait_minutes // 60
        mins = wait_minutes % 60
        avg_wait_str = f"{hours} ساعة و {mins} دقيقة" if hours > 0 else f"{mins} دقيقة"

        return render_template("kiosk.html", avg_wait_str=avg_wait_str)

    # ---------- Queue Display (page, Public) ----------
    @app.route("/queue")
    def queue():
        return render_template("queue.html")

    # ---------- Queue API (JSON for auto-refresh, Public) ----------
    @app.route("/api/queue")
    def api_queue():
        update_queue_priorities()
        from sqlalchemy import case as sa_case
        urgency_order = sa_case(
            (Patient.appointment_type == 'emergency', 1),
            (Patient.appointment_type == 'follow_up', 2),
            else_=3
        )
        in_progress_patients = Patient.query.filter_by(status="in_progress").order_by(Patient.check_in_time.asc()).all()
        waiting_patients = (
            Patient.query.filter_by(status="waiting")
            .order_by(urgency_order.asc(), Patient.priority_score.desc(), Patient.check_in_time.asc())
            .all()
        )
        patients = list(in_progress_patients) + list(waiting_patients)
        data = [
            {
                "id": p.id,
                "name": p.name,
                "age": p.age,
                "gender": p.gender,
                "appointment_type": p.appointment_type,
                "priority_score": p.priority_score,
                "status": p.status,
                "check_in_time": fmt_local(p.check_in_time),
            }
            for p in patients
        ]
        for i, item in enumerate(data):
            if item["status"] == "in_progress":
                item["wait_time"] = 0
                item["wait_duration"] = "-"
            else:
                item["wait_time"] = ai_engine.predict(i)
                item["wait_duration"] = wait_duration_str(patients[i].check_in_time)
        return jsonify(data)

    # ---------- Admin stats API (for Chart.js) ----------
    @app.route("/api/stats")
    def api_stats():
        emergency = Patient.query.filter_by(appointment_type="emergency").count()
        follow_up = Patient.query.filter_by(appointment_type="follow_up").count()
        checkup = Patient.query.filter_by(appointment_type="checkup").count()

        all_patients = Patient.query.all()
        today_local = to_local(now_utc())
        hours_map = {h: 0 for h in range(8, 23)}
        for p in all_patients:
            if p.check_in_time:
                h = to_local(p.check_in_time).hour  # تحويل إلى بغداد
                if h in hours_map:
                    hours_map[h] += 1

        today_str = today_local.strftime("%d/%m")
        def to_12h(h):
            suffix = "PM" if h >= 12 else "AM"
            h12 = h % 12 or 12
            return f"{h12:02d}:00 {suffix} - {today_str}"

        return jsonify({
            "labels": ["طوارئ", "متابعة", "كشف عادي"],
            "counts": [emergency, follow_up, checkup],
            "total_patients": len(all_patients),
            "waiting_count": Patient.query.filter_by(status="waiting").count(),
            "served_count": Patient.query.filter_by(status="done").count(),
            "busy_labels": [to_12h(h) for h in hours_map.keys()],
            "busy_counts": list(hours_map.values())
        })

    # ---------- AI Smart Insights API ----------
    @app.route("/api/ai_insights")
    @role_required("admin")
    def api_ai_insights():
        """
        نقطة نهاية الرؤى الذكية — تحلل النظام وتُنتج توصيات باللغة العربية.
        تستخدم تحليل البيانات الحي (Statistical Analysis) على معطيات الطابور الفعلية.
        """
        now = to_local(now_utc())
        insights = []

        waiting  = Patient.query.filter_by(status="waiting").all()
        done_all = Patient.query.filter_by(status="done").all()
        emergency_waiting = [p for p in waiting if p.appointment_type == "emergency"]
        followup_waiting  = [p for p in waiting if p.appointment_type == "follow_up"]
        checkup_waiting   = [p for p in waiting if p.appointment_type == "checkup"]

        # ── رؤية 1: مستوى الازدحام ───────────────────────────────────
        total_w = len(waiting)
        if total_w == 0:
            insights.append({"icon": "bi-check-circle-fill", "color": "green",
                             "text": "الطابور فارغ حالياً. لا يوجد مرضى في الانتظار."})
        elif total_w <= 3:
            insights.append({"icon": "bi-activity", "color": "blue",
                             "text": f"ضغط خفيف — {total_w} مرضى في الانتظار. الكفاءة ممتازة."})
        elif total_w <= 8:
            insights.append({"icon": "bi-exclamation-triangle-fill", "color": "yellow",
                             "text": f"ضغط متوسط — {total_w} مرضى ينتظرون. يُنصح بمتابعة التدفق بانتظام."})
        else:
            insights.append({"icon": "bi-fire", "color": "red",
                             "text": f"ضغط عالٍ — {total_w} مريضاً في الانتظار! يُوصى بالنظر في كادر إضافي."})

        # ── رؤية 2: حالات الطوارئ ────────────────────────────────────
        if emergency_waiting:
            names = "، ".join(p.name for p in emergency_waiting)
            insights.append({"icon": "bi-heart-pulse-fill", "color": "red",
                             "text": f"⚠ {len(emergency_waiting)} حالة طوارئ في الانتظار: {names} — يجب تقديمهم فوراً."})

        # ── رؤية 3: كبار السن في الانتظار ────────────────────────────
        elderly = [p for p in waiting if p.age >= 65]
        if elderly:
            insights.append({"icon": "bi-person-fill-gear", "color": "purple",
                             "text": f"يوجد {len(elderly)} مريض من كبار السن (65+) في الانتظار. أولوياتهم محسوبة تلقائياً."})

        # ── رؤية 4: أطول انتظار اليوم ────────────────────────────────
        if waiting:
            oldest = min(waiting, key=lambda p: p.check_in_time if p.check_in_time.tzinfo else
                         p.check_in_time.replace(tzinfo=__import__("datetime").timezone.utc))
            dur = wait_duration_str(oldest.check_in_time)
            insights.append({"icon": "bi-clock-history", "color": "orange",
                             "text": f"الأطول انتظاراً: {oldest.name} — منذ {dur}. تحقق من وضعه."})

        # ── رؤية 5: معدل الإنجاز اليوم ───────────────────────────────
        total_done = len(done_all)
        if total_done > 0:
            eff = round(total_done / max(total_done + total_w, 1) * 100)
            insights.append({"icon": "bi-graph-up-arrow", "color": "green",
                             "text": f"معدل إنجاز اليوم: {eff}٪ — تم الكشف على {total_done} مريض."})

        # ── رؤية 6: توزيع أنواع الزيارات ─────────────────────────────
        if total_w > 0:
            dominant = max(
                [("طوارئ", len(emergency_waiting)), ("متابعة", len(followup_waiting)), ("كشف عادي", len(checkup_waiting))],
                key=lambda x: x[1]
            )
            if dominant[1] > 0:
                pct = round(dominant[1] / total_w * 100)
                insights.append({"icon": "bi-bar-chart-fill", "color": "blue",
                                 "text": f"أغلب الحالات الحالية من نوع '{dominant[0]}' ({pct}٪ من الطابور)."})

        return jsonify({"insights": insights, "generated_at": now.strftime("%I:%M %p")})


    # ---------- Dashboards & Management ----------
    @app.route("/reception", methods=["GET", "POST"])
    @role_required("receptionist", "admin")
    def reception():
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            age = request.form.get("age", type=int)
            gender = request.form.get("gender", "male")
            appointment_type = request.form.get("appointment_type", "checkup")
            if not name or age is None:
                flash("الرجاء إدخال جميع الحقول.", "danger")
                return redirect(url_for("reception"))
            
            score = calculate_priority(age, appointment_type, 0)
            patient = Patient(name=name, age=age, gender=gender, appointment_type=appointment_type,
                             priority_score=score, check_in_time=now_utc())
            db.session.add(patient)
            db.session.commit()
            flash("تم تسجيل المريض بنجاح.", "success")
            return redirect(url_for("reception"))

        update_queue_priorities()
        from sqlalchemy import case as sa_case
        urgency_order = sa_case(
            (Patient.appointment_type == 'emergency', 1),
            (Patient.appointment_type == 'follow_up', 2),
            else_=3
        )
        patients = (
            Patient.query.filter(Patient.status.in_(["waiting", "in_progress"]))
            .order_by(urgency_order.asc(), Patient.priority_score.desc(), Patient.check_in_time.asc())
            .all()
        )

        wait_times = {}
        for index, p in enumerate(patients):
            if p.status == "in_progress":
                wait_times[p.id] = 0
            else:
                wait_times[p.id] = ai_engine.predict(index)

        return render_template("reception.html", patients=patients, wait_times=wait_times)

    @app.route("/reception/checkin/<int:patient_id>", methods=["POST"])
    @role_required("receptionist", "admin")
    def reception_checkin(patient_id):
        patient = Patient.query.get_or_404(patient_id)
        if patient.status == "scheduled":
            patient.status = "waiting"
            patient.check_in_time = now_utc()  # UTC — يعرض بتوقيت بغداد عبر الفلتر
            db.session.commit()
            flash(f"تم تسجيل حضور المريض {patient.name} وإضافته لقائمة الانتظار بنجاح.", "success")
        return redirect(url_for("reception"))

    # ── لوحة الطبيب: المريض الحالي والتالي وسجل اليوم ──
    @app.route("/doctor")
    @role_required("doctor", "admin")
    def doctor():
        """عرض لوحة الطبيب مع المريض الحالي والتالي وسجل كشوف اليوم."""
        update_queue_priorities()
        from sqlalchemy import case as sa_case
        urgency_order = sa_case(
            (Patient.appointment_type == 'emergency', 1),
            (Patient.appointment_type == 'follow_up', 2),
            else_=3
        )
        # المريض الحالي الذي بالعيادة الآن
        current = Patient.query.filter_by(status="in_progress").first()
        # المريض التالي في قائمة الانتظار
        next_patient = (
            Patient.query.filter_by(status="waiting")
            .order_by(urgency_order.asc(), Patient.priority_score.desc(), Patient.check_in_time.asc())
            .first()
        )
        # آخر موعد مسجل للمريض الحالي (للعرض في بطاقة المريض)
        last_appointment = (
            Appointment.query.filter_by(patient_id=current.id)
            .order_by(Appointment.scheduled_time.desc())
            .first()
        ) if current else None

        # ── سجل المرضى الذين تم كشفهم (status=done) مع آخر تشخيص لكل منهم ──
        done_patients = Patient.query.filter_by(status="done").order_by(Patient.check_in_time.desc()).all()
        # بناء dict: patient_id → آخر تشخيص نصي
        latest_diagnoses = {}
        for p in done_patients:
            # الحصول على آخر appointment يحتوي على ملاحظات للمريض
            appt = (
                Appointment.query.filter_by(patient_id=p.id)
                .filter(Appointment.notes.isnot(None))
                .filter(Appointment.notes != "")
                .order_by(Appointment.scheduled_time.desc())
                .first()
            )
            latest_diagnoses[p.id] = appt.notes if appt else None

        return render_template(
            "doctor.html",
            current=current,
            next_patient=next_patient,
            last_appointment=last_appointment,
            done_patients=done_patients,
            latest_diagnoses=latest_diagnoses,
        )

    # ── إنهاء الكشف الحالي وحفظ التشخيص ──
    @app.route("/doctor/finish", methods=["POST"])
    @login_required
    def doctor_finish():
        """ينهي الكشف الحالي ويحفظ التشخيص في جدول appointments."""
        diagnosis = request.form.get("diagnosis", "").strip()
        current = Patient.query.filter_by(status="in_progress").first()
        if current:
            # حفظ التشخيص فقط إذا كتب الطبيب نصاً
            if diagnosis:
                db.session.add(Appointment(
                    patient_id=current.id,
                    doctor_id=current_user.id,
                    scheduled_time=now_utc(),  # UTC دائماً
                    notes=diagnosis
                ))
            # تغيير حالة المريض إلى "انتهى"
            current.status = "done"
            db.session.commit()
            flash("تم إنهاء الكشف بنجاح.", "success")
        return redirect(url_for("doctor"))

    @app.route("/doctor/start", methods=["POST"])
    @login_required
    def doctor_start():
        current = Patient.query.filter_by(status="in_progress").first()
        if current:
            flash("يوجد مريض قيد الكشف بالفعل. قم بإنهاء الكشف أولاً.", "danger")
            return redirect(url_for("doctor"))

        from sqlalchemy import case as sa_case
        urgency_order = sa_case(
            (Patient.appointment_type == 'emergency', 1),
            (Patient.appointment_type == 'follow_up', 2),
            else_=3
        )
        next_p = (
            Patient.query.filter_by(status="waiting")
            .order_by(urgency_order.asc(), Patient.priority_score.desc(), Patient.check_in_time.asc())
            .first()
        )
        if next_p:
            next_p.status = "in_progress"
            db.session.commit()
            flash(f"تم إدخال المريض {next_p.name} للعيادة.", "info")
        else:
            flash("لا يوجد مرضى في قائمة الانتظار.", "warning")
        return redirect(url_for("doctor"))

    # ── لوحة الإدارة الرئيسية ──
    @app.route("/admin")
    @role_required("admin")
    def admin():
        """لوحة الإدارة: تعرض كل المرضى، المستخدمين، والإحصائيات وسجل التشخيصات."""
        update_queue_priorities()
        from sqlalchemy import case as sa_case
        urgency_order = sa_case(
            (Patient.appointment_type == 'emergency', 1),
            (Patient.appointment_type == 'follow_up', 2),
            else_=3
        )
        # جميع المرضى مرتبين حسب الأولوية
        patients = Patient.query.order_by(
            urgency_order.asc(), Patient.priority_score.desc(), Patient.check_in_time.asc()
        ).all()

        # جميع المستخدمين (بما فيهم المسؤولون) لعرضهم في جدول الإدارة
        users = User.query.order_by(User.role.asc(), User.username.asc()).all()

        # سجل التشخيصات (آخر 50 موعد)
        appointments = (
            Appointment.query
            .order_by(Appointment.scheduled_time.desc().nullslast(), Appointment.id.desc())
            .limit(50)
            .all()
        )

        waiting_count = Patient.query.filter_by(status="waiting").count()
        wait_minutes = ai_engine.predict(waiting_count)
        hours = wait_minutes // 60
        mins = wait_minutes % 60
        avg_wait_str = (
            f"{hours} ساعة و {mins} دقيقة" if hours > 0 else f"{mins} دقيقة"
        )

        # بناء قاموس مدة الانتظار لكل مريض في الطابور
        wait_durations = {p.id: wait_duration_str(p.check_in_time) for p in patients}

        return render_template(
            "admin.html",
            patients=patients,
            users=users,
            appointments=appointments,
            avg_wait_str=avg_wait_str,
            wait_durations=wait_durations,
        )


    # ── إنشاء مستخدم جديد (مع تحقق رمز المسؤول عند اختيار دور admin) ──
    @app.route("/admin/create_user", methods=["POST"])
    @role_required("admin")
    def admin_create_user():
        """إنشاء حساب مستخدم جديد مع تحقق خاص عند إنشاء مسؤول."""
        from flask import current_app
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        role = request.form.get("role", "doctor")
        admin_secret = request.form.get("admin_secret", "").strip()

        if not username or not password or not role:
            flash("يرجى ملء جميع الحقول", "danger")
            return redirect(url_for("admin"))

        # ── التحقق من رمز التفويض عند إنشاء حساب مسؤول ──
        if role == "admin":
            correct_key = current_app.config.get("ADMIN_SECRET_KEY", "")
            if admin_secret != correct_key:
                flash("رمز التفويض غير صحيح — لا يمكن إنشاء حساب مسؤول بدون الرمز الصحيح.", "danger")
                return redirect(url_for("admin"))

        if User.query.filter_by(username=username).first():
            flash("اسم المستخدم موجود مسبقاً", "danger")
            return redirect(url_for("admin"))

        new_user = User(username=username, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash(f"تم إضافة المستخدم '{username}' بنجاح", "success")
        return redirect(url_for("admin"))

    # ── حذف مستخدم (لا يمكن حذف المسؤولين) ──
    @app.route("/admin/users/<int:user_id>/delete", methods=["POST"])
    @role_required("admin")
    def admin_delete_user(user_id: int):
        """حذف مستخدم من النظام — المسؤولون محميون من الحذف."""
        user = User.query.get_or_404(user_id)
        if user.role == "admin":
            flash("لا يمكن حذف مستخدم مسؤول.", "danger")
            return redirect(url_for("admin"))
        db.session.delete(user)
        db.session.commit()
        flash(f"تم حذف المستخدم '{user.username}'.", "info")
        return redirect(url_for("admin"))

    # ── تغيير كلمة مرور مستخدم ──
    @app.route("/admin/users/<int:user_id>/password", methods=["POST"])
    @role_required("admin")
    def admin_change_password(user_id: int):
        """تغيير كلمة مرور مستخدم من لوحة الإدارة."""
        user = User.query.get_or_404(user_id)
        new_password = request.form.get("new_password", "").strip()
        if not new_password:
            flash("كلمة المرور الجديدة لا يمكن أن تكون فارغة.", "danger")
            return redirect(url_for("admin"))
        if len(new_password) < 3:
            flash("كلمة المرور يجب أن تكون 3 أحرف على الأقل.", "danger")
            return redirect(url_for("admin"))
        user.set_password(new_password)
        db.session.commit()
        flash(f"تم تغيير كلمة مرور '{user.username}' بنجاح.", "success")
        return redirect(url_for("admin"))

    @app.route("/admin/export_appointments")
    @role_required("admin")
    def export_appointments():
        """تصدير جدول التشخيصات كملف CSV للأرشفة."""
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["id", "patient_name", "doctor_username", "visit_time", "diagnosis"])
        for appointment in Appointment.query.order_by(Appointment.scheduled_time.desc().nullslast(), Appointment.id.desc()).all():
            patient_name = appointment.patient.name if appointment.patient else ""
            doctor_username = appointment.doctor.username if appointment.doctor else ""
            visit_time = appointment.scheduled_time.isoformat() if appointment.scheduled_time else ""
            diagnosis = appointment.notes or ""
            writer.writerow([appointment.id, patient_name, doctor_username, visit_time, diagnosis])

        response = make_response(output.getvalue())
        response.headers["Content-Type"] = "text/csv; charset=utf-8"
        response.headers["Content-Disposition"] = "attachment; filename=appointments.csv"
        return response

    # ── عارض قاعدة البيانات — يتيح رؤية وتعديل الجداول مباشرة ──
    @app.route("/admin/db")
    @role_required("admin")
    def db_viewer():
        """
        صفحة عارض قاعدة البيانات.
        تعرض جداول: patients, users, appointments مع إمكانية التعديل المباشر.
        للاستخدام التطويري والتجريبي فقط.
        """
        patients_all = Patient.query.order_by(Patient.id.desc()).all()
        users_all    = User.query.order_by(User.id.asc()).all()
        appts_all    = Appointment.query.order_by(Appointment.id.desc()).limit(100).all()
        return render_template(
            "db_viewer.html",
            patients=patients_all,
            users=users_all,
            appointments=appts_all,
        )

    # ── تعديل قيمة خلية مباشرة في DB (AJAX) ──
    @app.route("/admin/db/update", methods=["POST"])
    @role_required("admin")
    def db_update():
        """
        تحديث قيمة حقل واحد في أي جدول عبر AJAX.
        المدخلات (JSON): table, id, field, value
        """
        data  = request.get_json()
        table = data.get("table")
        row_id = data.get("id")
        field = data.get("field")
        value = data.get("value", "")

        # ── خريطة الجداول والحقول المسموح بتعديلها ──
        allowed = {
            "patients": ["name", "age", "gender", "appointment_type", "status", "priority_score"],
            "users":    ["username", "role"],
            "appointments": ["notes"],
        }
        if table not in allowed or field not in allowed[table]:
            return jsonify({"ok": False, "msg": "حقل غير مسموح بتعديله."})

        model = {"patients": Patient, "users": User, "appointments": Appointment}[table]
        obj = model.query.get(row_id)
        if not obj:
            return jsonify({"ok": False, "msg": "السجل غير موجود."})

        # تحويل النوع حسب الحقل
        if field in ("age", "priority_score"):
            try:
                value = int(value)
            except ValueError:
                return jsonify({"ok": False, "msg": "قيمة رقمية غير صالحة."})
        setattr(obj, field, value)
        db.session.commit()
        return jsonify({"ok": True, "msg": "✔ تم الحفظ."})

    # ── حذف سجل من جدول patients أو appointments ──
    @app.route("/admin/db/delete/<string:table>/<int:row_id>", methods=["POST"])
    @role_required("admin")
    def db_delete(table, row_id):
        """حذف سجل من DB مباشرة— للاستخدام التجريبي من واجهة عارض DB."""
        if table == "patients":
            obj = Patient.query.get_or_404(row_id)
        elif table == "appointments":
            obj = Appointment.query.get_or_404(row_id)
        else:
            flash("جدول غير مسموح بحذف سجلاته.", "danger")
            return redirect(url_for("db_viewer"))
        db.session.delete(obj)
        db.session.commit()
        flash(f"تم حذف السجل #{row_id} من جدول {table}.", "info")
        return redirect(url_for("db_viewer"))

    # ── صفحة التسجيل — يُعاد توجيهها للوحة الإدارة (يُنشأ المستخدمون من هناك) ──
    @app.route("/register")
    def register():
        """يُعيد التوجيه إلى لوحة الإدارة — المستخدمون يُنشأون من /admin فقط."""
        flash("إنشاء الحسابات يتم من لوحة الإدارة.", "info")
        return redirect(url_for("login"))

    # ── تسجيل الدخول ──
    @app.route("/login", methods=["GET", "POST"])
    def login():
        """صفحة تسجيل الدخول — تتحقق من الاسم وكلمة المرور وتُعيد توجيه حسب الدور."""
        if request.method == "POST":
            user = User.query.filter_by(username=request.form.get("username")).first()
            if user and user.check_password(request.form.get("password")):
                login_user(user)
                # توجيه المسؤول إلى لوحة الإدارة والبقية إلى لوحة الطبيب
                return redirect(url_for("admin" if user.role == "admin" else "doctor"))
        return render_template("login.html")

    # ── تسجيل الخروج ──
    @app.route("/logout")
    @login_required
    def logout():
        """إنهاء الجلسة وإعادة التوجيه لصفحة تسجيل الدخول."""
        logout_user()
        return redirect(url_for("login"))

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

