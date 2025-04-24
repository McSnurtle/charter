# How to use this dir?
Every python file in this directory should have a function called "calculate" within it. This function should accept a `pd.DataFrame` as it's first arg, and return `pd.DataFrame`.

The function should have the decorator `@register_indicator('example name')` where "example name" gets exposed to the end user. This is what registers the function as a valid indicator.

An example of a valid indicator file, would be:

```python
# imports
import pandas as pd


def calculate(df: pd.DataFrame, period: int = 50) -> pd.DataFrame:
    """Returns a dataframe with the same dimensions as the input of the simple moving average

    :param df: pd.DataFrame, the input chart data (return only calculates the ['close'].)
    :param period: int, the period to "roll over" when calculating the average."""

    return pd.DataFrame({
        'time': df['date'],
        f'SMA {period}': df['close'].rolling(window=period).mean()
    }).dropna()
```
