import os

from lightweight_charts import Chart


class Tag(str):
    def __init__(self, name: str = ""):
        self.value: str = name

    def get(self) -> str:
        return self.value


def save_drawings(symbol: str, interval: str, state: Chart) -> str | None:
    """Save drawings for a specific symbol and timeframe

    :return filename: str, the local path to the file where the drawings were stored."""
    filename = f"data/drawings/{symbol}_{interval}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    state.toolbox.save_drawings_under(Tag(filename))
    state.toolbox.export_drawings(os.path.abspath(Tag(filename)))

    return filename

def load_drawings(symbol: str, interval: str, state: Chart) -> str | None:
    """Load drawings for a specific symbol and timeframe

    :return filename: str, the local path to the file where the drawings were loaded from."""
    filename: str = f"data/drawings/{symbol}_{interval}.json"

    if not os.path.exists(filename):
        return None

    state.toolbox.import_drawings(os.path.abspath(filename))
    state.toolbox.load_drawings(Tag(filename))

    return filename
