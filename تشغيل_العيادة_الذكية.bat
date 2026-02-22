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
echo  [1/5] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    python3 --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo.
        echo  [!] Python is not installed on this machine!
        echo      Downloading and installing automatically...
        echo.

        REM Detect Architecture
        if "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
            set PY_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
        ) else (
            set PY_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9.exe
        )

        echo  [*] Downloading Python 3.11.9 from:
        echo      %PY_URL%
        echo.

        powershell -Command "& {Invoke-WebRequest -Uri '%PY_URL%' -OutFile '%TEMP%\python_installer.exe' -UseBasicParsing; Write-Host 'Download complete!'}"
        
        if %errorlevel% neq 0 (
            echo.
            echo  [Error] Failed to download Python. Check your internet connection.
            echo  Please download manually from: https://www.python.org/downloads/
            echo  (Remember to check "Add Python to PATH" during installation)
            pause
            exit /b 1
        )

        echo  [*] Installing Python silently and adding to PATH...
        "%TEMP%\python_installer.exe" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
        
        if %errorlevel% neq 0 (
            echo  [Error] Auto-install failed. Please run the installer manually.
            start "" "%TEMP%\python_installer.exe"
            echo  (Remember to check "Add Python to PATH" in the installer!)
            pause
            exit /b 1
        )

        REM Refresh environment variables for this session
        for /f "tokens=*" %%i in ('powershell -Command "[System.Environment]::GetEnvironmentVariable(\"PATH\",\"User\")"') do set "PATH=%%i;%PATH%"
        
        echo  [OK] Python installed successfully!
    )
)
echo  [OK] Python is installed.

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
echo  [3/5] Installing required libraries (Flask, AI, etc.)...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo  [Error] Failed to install libraries. Check your internet connection.
    pause
    exit /b 1
)
echo  [OK] All libraries installed successfully.

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
echo  [5/5] Starting Web Server...
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
