# src/utils/ui.py
# imports
import os
import platform
from tkinter import messagebox
from tkinter.simpledialog import askstring

from numpy import indices

# functions
def is_linux_x11():
    if platform.system() != "Linux":
        return False

    session_type = os.environ.get("XDG_SESSION_TYPE", "").lower()
    display = os.environ.get("DISPLAY", "")

    return session_type == "x11" or (session_type == "" and display.startswith(":"))

def open_indicator_selector(indicators: dict[str, bool]) -> dict[str, bool]:
    name = askstring(title="Indicator Selector", prompt="Enter the name of the indicator you would like to toggle:", initialvalue="e.g. SMA")
    if name in indicators.keys() and isinstance(name, str):     # if the input was successful (is str) and is a valid indicator name...
        # indicator status toggling
        if indicators[name]:
            indicators[name] = False
        elif not indicators[name]:
            indicators[name] = True
    else: popup(title="Indicator selection error", message=f"There was an error finding the indicator '{name}'. Please try again.", icon="error")
    return indicators

def popup(title: str = "Popup Notification", message: str = "", icon: str = "info", options: str = "ok") -> str | None:
    """Display a universal popup notification with the specified message

    :param title: str, the title of the popup window to be displayed
    :param message: str, the body text of the popup to be displayed
    :param icon: str, the preset icon to use in the popup, valid options are: [error, info, question, warning]. This may vary depending on operating system
    :param options: str, the preset of response options for the user, valid options are: [ok, okcancel, retrycancel, yesno, yesnocancel]"""

    return messagebox.Message(title=title, message=message, icon=icon, type=options).show()
