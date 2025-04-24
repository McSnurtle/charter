# charter
A lightweight, live chart analysis tool written entirely in vanilla python (maybe)!

![Screenshot_20250424_172921](https://github.com/user-attachments/assets/fdec11df-7eaa-47ec-ad70-12fe287ee577)

Using live data from the Yahoo! Finance API via the yfinance module, and the UI by TradingView's own Lightweight Charts API via the lightweight-charts-python wrapper: this sleek, live and intuitive chart analysis tool is sure to get you where you need to go, and further.

## Versioning
This project strictly adheres to the very real rules and regulations outlined in [this random stackoverflow comment](<https://softwareengineering.stackexchange.com/a/255201>) by "amon".
![image](https://github.com/user-attachments/assets/9946aa62-9155-4741-9335-16f8856c7f9e)

## What does this file / dir do?
### /data/
**Quick-access .csv files**
This directory stores caches of .csv data that gets downloaded from the Yahoo Finance API.
This is done to speed up the loading process of loading this data in the future.
The program checks if data from within the minute has already been downloaded - if so - it uses it instead of re-downloading the entire market's history. By default, the program will also purge any and all cached data of the same symbol and interval (i.e. NVDA-1D) that cannot be used (e.g. the data is too old)

### /data/cache/
**User configs**
Among others, the dir stores the user's last accessed symbol and interval, which is used for the next startup.

### /data/cache/drawings
**Permanent storage**
Storage for all of the user's chart drawings - automatically saved and applied between charts.

### /src/
**Where the main program files are stored**
The dir is home to all main program files used by and in the main thread.

### /src/utils
**Internal libraries**
Stores all of the mix-match of various functions and methods needed by the main program and it's files.

### /src/assets/
**UI**
Used to store various UI visual elements like fonts, images, and sounds for future updates.

### setup.sh
Installs and upgrades all dependencies of the program on startup, then runs it from the installed virtual environment.

### requirements.txt
A comprehensive list of all the basic dependencies of the program and their required version numbers.
