#!/bin/bash
source venv/bin/activate
pip install --upgrade --verbose -r requirements.txt
python src/main.py
