#src/utils/screenshot.py
# imports
import os
import datetime
from typing import List

from lightweight_charts import Chart


def save_screenshot(symbol: str, interval: str, state: Chart, format: str = "png") -> str | None:
    """Takes a screenshot of the current state of the chart and saves it.

    The filename is saved under f'data/screenshots/{symbol}-{interval}_{datetime.datetime.now()}.png'

    :param symbol: str, the symbol to save the filename as.
    :param interval: str, the interval to save the filename as.
    :param state: Chart, the UI object to screenshot.
    :param format: str, the image file format to save the screenshot as.

    :return filename: str, the filename of the image that was saved. Returns None if saving was unsuccessful."""

    today: str = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")
    filename: str = f"data/screenshots/{symbol.upper()}-{interval}_{today}.{format.lower()}"
    if not os.path.exists(filename):
        image: bytes = state.screenshot()
        with open(filename, 'wb') as file:
            file.write(image)
        return filename
    return


def list_screenshots() -> List[str]:
    """Returns a list of the filenames of all the screenshots the user has taken."""
    return os.listdir("data/screenshots/")
