# charter ⛵
A lightweight, live chart analysis tool written entirely in vanilla python (maybe)!

![Screenshot_20250424_172921](https://github.com/user-attachments/assets/fdec11df-7eaa-47ec-ad70-12fe287ee577)

Using live data from the Yahoo! Finance API via the [yfinance module](<https://github.com/ranaroussi/yfinance>), and the UI by TradingView's own Lightweight Charts API via the [lightweight-charts-python](<https://github.com/louisnw01/lightweight-charts-python>) wrapper: this sleek, live and intuitive chart analysis tool is sure to get you where you need to go, and further.

## Installation / Quick Start 🌨️
To install the project, first ensure you have it's sole dependency: [`Python3`](<https://www.python.org/downloads/>). Note that for automatic update checking and downloading

**1.** Clone the project
Press the big green Code button, then click download zip to install the source code, and extract the `.zip` file you download.
Alternatively, you can run `git clone https://github.com/McSnurtle/charter.git` to download the source directly.

**2.** Run the setup wizard
Depending on your platform, run the `setup.sh` or `setup.bat` files accordingly - `.sh` for unix based systems (macOS included), and `.bat` for windows.
This script executes the following commands (with some added juice) if you prefer to do this step manually:

for unix:
```shell
git fetch && git pull origin main \
python -m venv venv \
pip install --upgrade --verbose -r requirements.txt \
source ./venv/bin/activate \
python src/main.py
```

for windows:
```batch
git fetch; git pull origin main \
python -m venv venv \
pip install --upgrade --verbose -r requirements.txt \
call .\venv\Scripts\activate \
python src/main.py
```

## Usage 📈
### Chart Navigation
**Chart Navigation** is simple. To change the interval / timeframe, simply select your desired amount from the timeframe selector along the top of the window. To change what symbol you are viewing, simply start typing the name of the symbol, and 

| Hotkeys | Actions|
|---------|--------|
| `<Ctrl>+F` | Search for symbol |
| `<Ctrl>+R` | Refresh price data |
| `<Ctrl>+P` | Save screenshot |
| `<Ctrl>+I` | Search for indicators |

### Chart Annotations
**Chart Annotations** can be made by using the drawing toolbox located on the left hand side of the screen. To start a drawing, click, then click again to end it. Note: sometimes drawings will be cancelled if the mouse is subtly moved during a click or is released too fast.

| Hotkeys | Actions|
|---------|--------|
| `<Alt>+T` | Trendline |
| `<Alt>+H` | Horizontal Line |
| `<Alt>+R` | Ray Line |
| `<Ctrl>+Z` | Undo |
| `<Ctrl>+S` | Save current drawings |
| `<Ctrl>+L` | Load saved drawings |

## Versioning
This project strictly adheres to the very real strict rules and regulations outlined in [this random stackoverflow comment](<https://softwareengineering.stackexchange.com/a/255201>) by "amon" and loosely follows the project structuring guide as outlined in [AlexDCode/Software-Development-Project-Structure](<https://github.com/AlexDCode/Software-Development-Project-Structure/tree/master>).
![image](https://github.com/user-attachments/assets/9946aa62-9155-4741-9335-16f8856c7f9e)

## Configuration
Below are all of the configuration options (as found in `etc/preferences.json`, their defaults, and what they do to the program:

| Name | Default | Description |
|------|---------|-------------|
| `chart[refresh_rate]` | `30` | The rate in seconds that the program will wait to refresh the market history / data. The minimum is 60.
| `copy_screenshots` | `true` | Whether when taking screenshots of the chart with `<Ctrl>+P`, the program should also copy the image to the system clipboard. |

## What does this file / dir do?
- `data/`
**Quick-access .csv files**
This directory stores caches of .csv data that gets downloaded from the Yahoo Finance API.
This is done to speed up the loading process of loading this data in the future.
The program checks if data from within the minute has already been downloaded - if so - it uses it instead of re-downloading the entire market's history. By default, the program will also purge any and all cached data of the same symbol and interval (i.e. NVDA-1D) that cannot be used (e.g. the data is too old)

- `data/drawings/`
**Permanent storage**
Storage for all of the user's chart drawings - automatically saved and applied between charts.

- `data/screenshots/`
**Image storage**
The final destination for all the user's chart screenshots. The images are also copied to the system clipboard if the feature is enabled in `etc/preferences.json`

- `src/`
**Where the main program files are stored**
The dir is home to all main program files used by and in the main thread.

- `src/utils`
**Internal libraries**
Stores all of the mix-match of various functions and methods needed by the main program and it's files.

- `src/assets/`
**UI**
Used to store various UI visual elements like fonts, images, and sounds for future updates.

- `setup.sh` & `setup.bat`
Installs and upgrades all dependencies of the program on startup, then runs it from the installed virtual environment.

- `requirements.txt`
A comprehensive list of all the basic dependencies of the program and their required version numbers.
