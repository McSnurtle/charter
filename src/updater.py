#src/updater.py
# imports
import os
import sys

from utils.platform import popup


def main() -> None:
    question: str | None = popup(title="Update Checker", message="An update has been found for charter: {} (local) vs {} (remote)\n\nWould you like to download it now? Selecting 'No' will continue to the currently installed version.", icon="info", options="yesnocancel")
    if not isinstance(question, str):
        sys.exit(2) # equivalent to "cancel"
    
    if question == "yes":
        sys.exit(0)
    elif question == "no":
        sys.exit(1)
    elif question == "cancel":
        sys.exit(2)


if __name__ == "__main__":
    main()
    