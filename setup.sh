#!/bin/bash
if [ ! -d "venv"]; then
    echo "Creating virtual environment"
    python --verbose -m venv venv
fi

source venv/bin/activate
pip install --upgrade --verbose -r requirements.txt
export PYWEBVIEW_GUI=qt
python src/main.py
