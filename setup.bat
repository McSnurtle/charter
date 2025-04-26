@echo off
setlocal enabledelayedexpansion

:: Update checker
echo Checking for updates
git fetch 

for /f %%i in ('git rev-parse @') do set LOCAL=%%i
for /f %%i in ('git rev-parse @{u}') do set REMOTE=%%i
for /f %%i in ('git merge-base @ @{u}') do set BASE=%%i

if "%LOCAL%" == "%REMOTE%" (
    echo Up to date
) else if "%LOCAL%" == "%BASE%" (
    echo Update found

    python3 src/updater.py
    set PY_RET=%ERRORLEVEL%

    if "!PY_RET!" == "0" (
        echo Downloading update
        git pull
    ) else if "!PY_RET!" == "1" (
        echo Skipping update
    ) else if "!PY_RET!" == "2" (
        echo Operation cancelled
        exit /b 0
    )
) else (
    echo Local is ahead of remote, skipping update check
)

:: Init
echo Attempting creation of virtual environment
python3 -m venv venv
call .\venv\Scripts\activate
pip3 install --upgrade --verbose -r requirements.txt
python3 src/main.py
