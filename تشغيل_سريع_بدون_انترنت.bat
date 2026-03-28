@echo off
REM Change working directory to the script's location
cd /d "%~dp0"

title Smart Clinic System - Auto Launcher
cls
echo.
echo  ==========================================================
echo            Smart Clinic System - Auto Launcher             
echo  ==========================================================
echo.

REM -----------------------------------------------------
REM 1. Check Python
REM -----------------------------------------------------
echo  [1/3] Checking Python installation... 
python --version

REM -----------------------------------------------------
REM 2. Check/Create Virtual Environment
REM -----------------------------------------------------
echo.
echo  [2/5] Checking Virtual Environment (venv)...
if not exist "venv\Scripts\activate.bat" (
    echo  [*] Creating a new isolated Python virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo  [Error] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo  [OK] Virtual environment created successfully.
) else (
    echo  [OK] Virtual environment already exists.
)

REM -----------------------------------------------------
REM 3. Activate venv ^& Install Libraries
REM -----------------------------------------------------
echo.
echo  [2/3] Activating... 
call venv\Scripts\activate.bat

REM -----------------------------------------------------
REM 4. Setup Database
REM -----------------------------------------------------
echo.
echo  [4/5] Setting up the Virtual Clinic Database...
if not exist clinic.db (
    echo  [*] Database not found. Creating it with sample data...
    python seed_db.py
    if %errorlevel% neq 0 (
        echo  [Warning] Demo data script failed - the clinic will start empty.
    ) else (
        echo  [OK] Database created successfully with demo accounts:
        echo       - Admin:     admin     / 123
        echo       - Doctor:    doctor    / 123
        echo       - Reception: reception / 123
    )
) else (
    echo  [OK] Database already exists.
)

REM -----------------------------------------------------
REM 5. Start Server ^& Open Browser
REM -----------------------------------------------------
echo.
echo  [3/3] Starting Web Server...
echo.
echo  ==========================================================
echo   [OK] System is ready! Opening browser at:
echo     http://127.0.0.1:8080
echo.
echo   Login Details:
echo     Admin     -^> admin      / 123
echo     Doctor    -^> doctor     / 123
echo     Reception -^> reception  / 123
echo.
echo   To stop the system: Press Ctrl+C in this window.
echo  ==========================================================
echo.

REM Open browser after 2 seconds
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8080"

REM Run server
python main.py

echo.
echo  [!] Server stopped. You can close this window.
pause

