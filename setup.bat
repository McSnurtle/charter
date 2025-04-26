@echo on
echo Attempting creation of virtual environment
python3 -m venv venv
call .\venv\Scripts\activate
pip3 install --upgrade --verbose -r requirements.txt
python3 src/main.py
