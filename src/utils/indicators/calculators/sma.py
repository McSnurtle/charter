# imports
import pandas as pd
from utils.indicators import registry


@registry.register_indicator("SMA")
def calculate(df: pd.DataFrame, period: int = 50) -> pd.DataFrame:
    """Returns a dataframe with the same dimensions as the input of the simple moving average

    :param df: pd.DataFrame, the input chart data (return only calculates the ['close'].)
    :param period: int, the period to "roll over" when calculating the average."""

    return pd.DataFrame({
        'time': df['date'],
        'SMA': df['close'].rolling(window=period).mean()
    }).dropna()
