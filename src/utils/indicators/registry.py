# imports
from typing import Any, Callable

# vars
indicators: dict[str, Callable] = {}

# functions
def list_names() -> list[str]:
    return list(indicators.keys())

def list_functions() -> list[Callable]:
    return list(indicators.values())

def get_function(name: str) -> Callable:
    return indicators[name]

def register_indicator(self, name: Any = None):
    """Used to regiter a decorater to the Register() under a specific name.

    :param name: str, the name to register the function under.
    :return decorator:

    example usage:
    ```
    @register_indicator('Simple Moving Average')
    def calculate_sma(df: pd.DataFrame, period: int = 50) -> pd.Series:
        return df['close'].rolling(window=period).mean().rename('SMA')
    ```
    This will register the function under the name 'Simple Moving Average' where the line will be plotted as 'SMA' on the chart view."""
    def decorator(func: Callable):
        indicator_name = name or func.__name__
        self[indicator_name] = func
        return func
    return decorator
