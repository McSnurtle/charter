# imports
import sys
import os
from threading import Thread
from time import sleep
from typing import Any

from utils.scrape import get_historical
from utils.ui import popup

import pandas as pd
from lightweight_charts import Chart


class UI(Chart):

    REFRESH_RATE: int = 30   # time to wait (seconds) between refreshing the markets. Min: 1min
    SCRAPING: bool = True   # should the market scraping be live?
    SYMBOL: str = "BTC-USD"
    INTERVAL: str = "1d"

    def __init__(self, symbol: str = "BTC-USD"):
        super().__init__(toolbox=True)
        # init
        self.dataframe: pd.DataFrame = pd.DataFrame()
        self.update_chart()
        if not isinstance(self.dataframe, pd.DataFrame) or self.dataframe.empty:        # if there is an error...
            popup("Data Error", f"There was an error retrieving the market data for symbol '{symbol}'. Please check the logs for more information", icon="error")
            self.kill()

        self.legend(True)
        self.set(df=self.dataframe)
        self.update_watermark()
        self.topbar.textbox('symbol', symbol)
        self.topbar.switcher('timeframe', ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '4h', '1d', '5d', '1wk', '1mo', '3mo'), default='1d', func=self.on_timeframe_change)

        self.events.search += self.on_search
        self.hotkey("ctrl", "R", self.refresh)

        # vars
        self.threads: list[Thread] = []

    def on_search(self, state: Any, searched_string: str) -> None:
        symbol = self.SYMBOL
        self.SYMBOL = searched_string
        if not self.refresh(keep_drawings=False):   # if the new symbol data doesn't exist
            self.SYMBOL = symbol
            self.refresh(keep_drawings=False)
        self.topbar['symbol'].set(self.SYMBOL)

    def on_timeframe_change(self, state: Any) -> None:
        self.INTERVAL = self.topbar['timeframe'].value
        self.refresh()

    def scrape_loop(self) -> None:
        while self.SCRAPING:
            print(f"Pulling new data to dataframe on ticker {self.SYMBOL.upper()}-{self.INTERVAL.upper()}...")
            self.update_chart(keep_drawings=True)

            sleep(self.REFRESH_RATE)

    def update_chart(self, keep_drawings: bool = False) -> pd.DataFrame | None:
        df: pd.DataFrame = get_historical(symbol=self.SYMBOL, interval=self.INTERVAL)
        if isinstance(df, pd.DataFrame) and not df.empty:
            self.dataframe = df
            self.set(df=self.dataframe, keep_drawings=keep_drawings)
            return df
        else:
            popup("Data Error", f"There was an error retrieving the market data for symbol '{self.SYMBOL}'. Please check the logs for more information", icon="error")
            return None

    def update_watermark(self) -> str:
        self.watermark(f"{self.SYMBOL} {self.INTERVAL.upper()}", color="rgba(100, 100, 120, 0.4)")
        return f"{self.SYMBOL} {self.INTERVAL.upper()}"

    def refresh(self, keep_drawings: bool = True) -> bool:
        """Returns true if the chart was able to refresh and retrieve new data"""
        # self.win.run_script("document.body.style.cursor = 'wait';")
        self.spinner(True)
        self.update_watermark()
        result = self.update_chart(keep_drawings=keep_drawings)
        # self.win.run_script("document.body.style.cursor = 'default';")
        self.spinner(False)
        if isinstance(result, pd.DataFrame):
            return True
        return False

    def start_loop(self) -> Thread:
        scrape_thread: Thread = Thread(target=self.scrape_loop)
        scrape_thread.start()
        self.threads.append(scrape_thread)

        return scrape_thread

    def kill(self) -> None:
        self.SCRAPING = False
        self.exit()
        sys.exit(1)


if __name__ == "__main__":
    root = UI(symbol="BTC-USD")
    root.start_loop()
    root.show(block=True)
