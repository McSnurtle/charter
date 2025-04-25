@echo on
if not exist venv\ (
    echo Creating virtual environment
    python --verbose -m venv venv
)

.\venv\Scripts\activate
pip install --upgrade --verbose -r requirements.txt
python src/main.py
