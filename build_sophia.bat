@echo off
echo [*] INITIATING SOVEREIGN COMPILATION PROTOCOL...

:: Ensure PyInstaller is installed
python -m pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] PyInstaller not found. Installing...
    python -m pip install pyinstaller
)

:: Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.spec" del "*.spec"

:: Compile
echo [*] Compiling sophia/main.py -> sophia.exe...
python -m PyInstaller --noconfirm --onefile --console --name "sophia" --icon "NONE" --hidden-import "rich" --clean "sophia/main.py"

echo.
if exist "dist\sophia.exe" (
    echo [SUCCESS] Build Complete.
    echo Target: dist\sophia.exe
    echo.
    echo [NOTE] Remember to copy .env and .md files to dist/ if needed.
) else (
    echo [FAILURE] Build Failed. Check logs.
)
pause
