#!/bin/bash
if [ ! -d "./venv" ]; then
    echo "Creating virtual environment"
    python3 --verbose -m venv venv
fi

source venv/bin/activate
pip3 install --upgrade --verbose -r requirements.txt
export PYWEBVIEW_GUI=qt
python3 src/main.py
