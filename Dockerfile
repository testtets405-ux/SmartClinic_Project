# ================================================================================
# Dockerfile لإعداد تطبيق العيادة الذكية على منصة Hugging Face Spaces
# ================================================================================

# 1. استخدام نسخة مستقرة من Python 3.11 (نسخة كاملة لضمان سرعة بناء المكتبات)
FROM python:3.11

# تفعيل تسجيل اللوحات (Logging) بشكل فوري ومنع تخزينها مؤقتاً
ENV PYTHONUNBUFFERED=1

# 2. إعداد مستخدم غير جذري (Non-root user) لمتطلبات الأمان في Hugging Face
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# 3. تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# 4. نسخ ملف المتطلبات وتثبيت المكتبات
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 5. نسخ كافة ملفات المشروع إلى الحاوية
COPY --chown=user . .

# 6. إعداد المنفذ الافتراضي لـ Hugging Face (7860)
EXPOSE 7860

# 7. أمر التشغيل باستخدام Gunicorn لضمان استقرار الموقع في بيئة الإنتاج
# نستخدم --bind 0.0.0.0:7860 لربط التطبيق بالمنفذ الصحيح
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:7860", "--workers", "2", "--timeout", "120"]
