@echo on
if not exist venv\ (
    echo Creating virtual environment
    python3 --verbose -m venv venv
)

.\venv\Scripts\activate
pip3 install --upgrade --verbose -r requirements.txt
python3 src/main.py
