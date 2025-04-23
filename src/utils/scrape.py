# imports
import datetime
import os
# from typing import Any
from pathlib import Path

import pandas as pd
import yfinance as yf


def get_historical(period: str = "max", symbol: str = "BTC-USD", interval: str = "1d", save: bool = True) -> pd.DataFrame | None | pd.Series:
    """Return historical pd.DataFrame of ticker price and volume history for the specified params.

    :param period: str, must be of the format 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max, etc.
    :param symbol: str, name of stock / currency to track, e.g. "AAPL
    :param interval: str, Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 4h, 1d, 5d, 1wk, 1mo, 3mo]
    """

    today: str = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")
    filename: str = f"{symbol.upper()}-{interval}_{today}"
    # I sincerely apologize for the excessive typing here. Below is the fault of Zeditor for using PyRight and not letting me do anything unless all types are fully and completely satisfied without any chance for ambiguity
    if not cached(filename, purge=True):    # if the same dataframe from within the minute does not already exist...
        data: pd.DataFrame | None | pd.Series = yf.download(tickers=symbol, period=period, interval=interval)
        if isinstance(data, pd.DataFrame) and not data.empty:
            # formatting
            data: pd.DataFrame | None | pd.Series = data[["Open", "High", "Low", "Close", "Volume"]].copy()
            data.reset_index(inplace=True)
            data.columns = ["date", "open", "high", "low", "close", "volume"]
            # caching
            if save:
                data.to_csv(f"data/{filename}.csv")
        else:
            print("WARN: Somehow data object is of type None from method get_historical!")
            return
    else:   # if the same data from within the minute does already exist...
        data: pd.DataFrame | None | pd.Series = pd.read_csv(f"data/{filename}.csv")

    return data


def cached(file: str, purge: bool = False) -> bool:
    """Checks the /data dir for previously cached versions of the same dataset. Only checks for csv files

    :param file: str, the name of the dataset to check against.
    :param purge: bool, if all irrelevant datasets of the same name (the NAME in NAME_DATE_TIME) should be deleted from the /data dir.
    :return exists: bool, whether the dataset pre-exists or not."""

    exists: bool  = os.path.exists(f"data/{file}.csv")
    if purge:
        # CREDIT: Sam Bull on stackoverflow.com
        for path in Path("data/").glob(f"{file.split('_')[0]}*.csv"):   # get all files matching pattern "data/NAME*.csv"
            if str(path) != f"data/{file}.csv":  # if the irrelevant dataset is NOT the same as the selected dataset...
                path.unlink()   # delete them from exinistence

    return exists
