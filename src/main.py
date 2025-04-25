#src/main.py
# imports
import sys
from threading import Thread
from time import sleep
from typing import Any, Callable

from utils.indicators import registry as indicators
from utils.scrape import get_historical
from utils.platform import get_preferences, popup
from utils.drawings import save_drawings, load_drawings

import pandas as pd
from lightweight_charts import Chart


class UI(Chart):

    REFRESH_RATE: int = 60   # time to wait (seconds) between refreshing the markets. Min: 1min
    SYMBOL: str = "BTC-USD"
    INTERVAL: str = "1d"
    DRAWING_MODE: str = "none"

    def __init__(self, config: dict[str, Any] = {}, symbol: str = "BTC-USD"):
        super().__init__(toolbox=True)
        # init
        self.dataframe: pd.DataFrame = pd.DataFrame()
        self.config: dict[str, Any] = config
        self.indicators: dict[str, bool] = {}
        self.drawings: list[dict] = []
        self.threads: list[Thread] = []
        self.update_chart()
        if not isinstance(self.dataframe, pd.DataFrame) or self.dataframe.empty:        # if there is an error...
            popup("Data Error", f"There was an error retrieving the market data for symbol '{symbol}'. Please check the logs for more information", icon="error")
            self.kill()

        self.legend(True)
        self.set(df=self.dataframe)
        self.update_watermark()
        self.topbar.textbox('symbol', symbol)
        self.topbar.menu("indicators", options=indicators.list_names(), default="SMA", func=self.set_indicator)
        self.topbar.switcher('timeframe', ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '4h', '1d', '5d', '1wk', '1mo', '3mo'), default='1d', func=self.on_timeframe_change)

        self.events.search += self.on_search
        self.hotkey("ctrl", "R", self.refresh)
        self.hotkey("ctrl", "S", self.save_current_drawings)
        self.hotkey("ctrl", "L", self.load_saved_drawings)

        self.init_data()

    def on_search(self, state: Any, searched_string: str) -> None:
        symbol = self.SYMBOL
        self.SYMBOL = searched_string
        if not self.refresh(keep_drawings=False):   # if the new symbol data doesn't exist
            self.SYMBOL = symbol
            self.refresh(keep_drawings=False)
        self.topbar['symbol'].set(self.SYMBOL)

    def on_timeframe_change(self, state: Any) -> None:
        self.INTERVAL = self.topbar['timeframe'].value
        self.refresh(keep_drawings=False)


    def set_indicator(self, callback: Any) -> None:
        indicator_name: str = self.topbar['indicators'].value
        line = self.create_line(name=indicator_name, width=2, style='solid')
        calculator: Callable = indicators.get_function(name=indicator_name)
        data: pd.DataFrame = calculator(self.dataframe)
        line.set(data)

    def init_data(self) -> None:
        self.init_config()

        self.update_chart()
        if not isinstance(self.dataframe, pd.DataFrame) or self.dataframe.empty:        # if there is an error...
            popup("Data Error", f"There was an error retrieving the market data for symbol '{self.symbol}'. Please check the logs for more information", icon="error")
            self.kill()

        scrape_thread: Thread = Thread(target=self.scrape_loop)
        scrape_thread.start()
        self.threads.append(scrape_thread)

        self.load_saved_drawings()

    def init_config(self) -> dict[str, Any]:
        self.REFRESH_RATE = self.config['chart']['refresh_rate']
        return self.config

    def scrape_loop(self) -> None:
        while self.is_alive:
            print(f"Pulling new data to dataframe on ticker {self.SYMBOL.upper()}-{self.INTERVAL.upper()}...")
            self.update_chart(keep_drawings=True)

            sleep(self.REFRESH_RATE)

    def update_chart(self, keep_drawings: bool = False) -> pd.DataFrame | None:
        df: pd.DataFrame = get_historical(symbol=self.SYMBOL, interval=self.INTERVAL)
        if isinstance(df, pd.DataFrame) and not df.empty:
            self.dataframe = df
            self.set(df=self.dataframe, keep_drawings=keep_drawings)

            # Load saved drawings if not keeping existing ones
            if not keep_drawings:
                self.load_saved_drawings()

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
        self.save_current_drawings()
        result = self.update_chart(keep_drawings=keep_drawings)
        # self.win.run_script("document.body.style.cursor = 'default';")
        self.load_saved_drawings()
        self.spinner(False)
        if isinstance(result, pd.DataFrame):
            return True
        return False

    def kill(self) -> None:
        print("WARN | KILLING SELF!")
        self.SCRAPING = False
        self.exit()
        sys.exit(1)

    def save_current_drawings(self, state: Any = None) -> None:
        """Save current chart drawings"""
        path = save_drawings(self.SYMBOL, self.INTERVAL, self)
        print(f"DEBUG: saving drawings to '{path}'")

    def load_saved_drawings(self, state: Any = None) -> None:
        """Load saved drawings for current symbol/interval"""
        path = load_drawings(self.SYMBOL, self.INTERVAL, self)
        print(f"DEBUG: loading drawings from '{path}'")


if __name__ == "__main__":
    print(f"Using indicator set: {indicators.list_names()}...")
    print(f"Using config: {get_preferences()}")

    root = UI(config=get_preferences(), symbol="BTC-USD")
    root.show(block=True)
