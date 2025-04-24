# imports
import os
from importlib import import_module

from typing import Any, Callable

def list_names() -> tuple[str] | tuple[object, ...]:
    return tuple(indicators.keys())

def list_functions() -> list[Callable]:
    return list(indicators.values())

def get_function(name: str) -> Callable:
    return indicators[name]

def register_indicator(name: Any = None):
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
        indicators[indicator_name] = func
        return func
    return decorator

# init
if __name__ != "__main__":
    print("amogus")
    indicators: dict[str, Callable] = {}
    calculators: str = os.path.join(os.path.dirname(__file__), "calculators")
    print(f"DEBUG CALCULATORS: {calculators}")
    for script in os.listdir(calculators):
        print(f"DEBUG SCRIPTS: {script}")
        if script.endswith('.py'):
            print(f"DEBUG IMPORTING: {script}")
            import_module(f"utils.indicators.calculators.{script[:-3]}")  # remove .py to only run `import script` and not `import script.py`
