#!/bin/bash
source venv/bin/activate
pip install --upgrade --verbose -r requirements.txt
export PYWEBVIEW_GUI=qt
python src/main.py
