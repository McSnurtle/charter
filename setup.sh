#!/bin/bash

# update checking
echo "Checking for updates"
git fetch

LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})
BASE=$(git merge-base @ @{u})

if [ "$LOCAL" = "$REMOTE" ]; then
    echo "Up to date"
elif [ "$LOCAL" = "$BASE" ]; then
    echo "Update found"
    python3 src/updater.py
    PY_RET=$?

    if [ "$PY_RET" -eq 0 ]; then
        echo "Downloading update"
        git pull
    elif [ "$PY_RET" -eq 1 ]; then
        echo "Skipping update"
    elif [ "$PY_RET" -eq 2 ]; then
        echo "Operation cancelled"
        exit 0
    fi
else
    echo "Local is ahead of remote, skipping update check"
fi

# init
echo "Attempting creation of virtual environment"
python3 -m venv venv
source venv/bin/activate
echo "Upgrading dependencies"
pip3 install --upgrade --verbose -r requirements.txt
export PYWEBVIEW_GUI=qt
python3 src/main.py
