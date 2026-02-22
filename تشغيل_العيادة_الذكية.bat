@echo off
chcp 65001 >nul 2>&1
title نظام العيادة الذكية - Smart Clinic

cls
echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║       نظام العيادة الذكية - Smart Clinic System         ║
echo  ║              سكربت التشغيل التلقائي الشامل              ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.

REM ─────────────────────────────────────────────────────
REM 1. التحقق من وجود Python على الجهاز
REM ─────────────────────────────────────────────────────
echo  [1/5] التحقق من بايثون (Python)...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    python3 --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo.
        echo  [!] بايثون غير مثبت على هذا الجهاز!
        echo      سيتم تحميله وتثبيته تلقائياً من الموقع الرسمي...
        echo.

        REM تحديد معمارية الجهاز
        if "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
            set PY_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
        ) else (
            set PY_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9.exe
        )

        echo  [*] جاري تحميل Python 3.11.9 من:
        echo      %PY_URL%
        echo.

        REM استخدام PowerShell للتحميل
        powershell -Command "& {Invoke-WebRequest -Uri '%PY_URL%' -OutFile '%TEMP%\python_installer.exe' -UseBasicParsing; Write-Host 'تم التحميل بنجاح!'}"
        
        if %errorlevel% neq 0 (
            echo.
            echo  [خطأ] فشل تحميل بايثون. تحقق من اتصالك بالإنترنت.
            echo  يمكنك تحميله يدوياً من: https://www.python.org/downloads/
            echo  (تذكر: ضع علامة على "Add Python to PATH" عند التثبيت)
            pause
            exit /b 1
        )

        echo  [*] جاري تثبيت Python بشكل صامت مع إضافته لـ PATH...
        "%TEMP%\python_installer.exe" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
        
        if %errorlevel% neq 0 (
            echo  [خطأ] فشل التثبيت التلقائي. يرجى تشغيل المثبت يدوياً.
            start "" "%TEMP%\python_installer.exe"
            echo  (لا تنسَ تفعيل "Add Python to PATH" في المثبت!)
            pause
            exit /b 1
        )

        REM تحديث متغيرات البيئة في هذه الجلسة
        for /f "tokens=*" %%i in ('powershell -Command "[System.Environment]::GetEnvironmentVariable(\"PATH\",\"User\")"') do set "PATH=%%i;%PATH%"
        
        echo  [✓] تم تثبيت Python بنجاح!
    )
)
echo  [✓] Python موجود على الجهاز.

REM ─────────────────────────────────────────────────────
REM 2. التحقق أو إنشاء البيئة الافتراضية
REM ─────────────────────────────────────────────────────
echo.
echo  [2/5] التحقق من البيئة الافتراضية (venv)...
if not exist "venv\Scripts\activate.bat" (
    echo  [*] إنشاء بيئة بايثون افتراضية منعزلة جديدة...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo  [خطأ] فشل إنشاء البيئة الافتراضية.
        pause
        exit /b 1
    )
    echo  [✓] تم إنشاء البيئة الافتراضية بنجاح.
) else (
    echo  [✓] البيئة الافتراضية موجودة مسبقاً.
)

REM ─────────────────────────────────────────────────────
REM 3. تفعيل البيئة وتثبيت المكتبات
REM ─────────────────────────────────────────────────────
echo.
echo  [3/5] تثبيت المكتبات المطلوبة (Flask, AI, والباقي)...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo  [خطأ] فشل تثبيت المكتبات. تحقق من اتصالك بالإنترنت.
    pause
    exit /b 1
)
echo  [✓] جميع المكتبات مثبتة بنجاح.

REM ─────────────────────────────────────────────────────
REM 4. تجهيز قاعدة البيانات
REM ─────────────────────────────────────────────────────
echo.
echo  [4/5] تجهيز قاعدة البيانات...
if not exist clinic.db (
    echo  [*] قاعدة البيانات غير موجودة.. يتم إنشاؤها بمرضى وحسابات تجريبية...
    python seed_db.py
    if %errorlevel% neq 0 (
        echo  [تحذير] لم يتم تشغيل سكربت البيانات التجريبية - ستبدأ العيادة فارغة تماماً.
    ) else (
        echo  [✓] تم إنشاء قاعدة البيانات بنجاح مع البيانات التجريبية:
        echo       - المدير:    admin    / 123
        echo       - الطبيب:   doctor   / 123
        echo       - الاستقبال: reception / 123
    )
) else (
    echo  [✓] قاعدة البيانات موجودة مسبقاً.
)

REM ─────────────────────────────────────────────────────
REM 5. تشغيل الخادم وفتح المتصفح
REM ─────────────────────────────────────────────────────
echo.
echo  [5/5] تشغيل الخادم...
echo.
echo  ══════════════════════════════════════════════════════════
echo   ✓ النظام جاهز! سيتم فتح المتصفح على:
echo     http://127.0.0.1:8080
echo.
echo   بيانات الدخول:
echo     المدير    →  admin      / 123
echo     الطبيب   →  doctor     / 123
echo     الاستقبال →  reception  / 123
echo.
echo   لإيقاف النظام: اضغط Ctrl+C في هذه النافذة
echo  ══════════════════════════════════════════════════════════
echo.

REM فتح المتصفح بعد ثانيتين
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8080"

REM تشغيل السيرفر
python main.py

echo.
echo  [!] تم إيقاف الخادم. يمكنك إغلاق هذه النافذة.
pause
