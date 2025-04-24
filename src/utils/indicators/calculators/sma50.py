#src/utils/indicators/calculators/sma50.py
# imports
import pandas as pd
from utils.indicators import registry


@registry.register_indicator("SMA 50")
def calculate(df: pd.DataFrame) -> pd.DataFrame:
    """Returns a dataframe with the same dimensions as the input of the simple moving average

    :param df: pd.DataFrame, the input chart data (return only calculates the ['close'].)
    """

    return pd.DataFrame({
        'time': df['date'],
        'SMA 50': df['close'].rolling(window=50).mean()
    }).dropna()
