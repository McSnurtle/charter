#!/bin/bash
echo "Checking for updates"
git fetch; git pull origin main
echo "Attempting creation of virtual environment"
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade --verbose -r requirements.txt
export PYWEBVIEW_GUI=qt
python3 src/main.py
