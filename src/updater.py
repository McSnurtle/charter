#src/updater.py
# imports
import json
import sys
import subprocess
from subprocess import CompletedProcess
from typing import Any

from utils.platform import popup


def get_ref_version(branch: str = "main") -> str:    
    subprocess.run(("git", "fetch"), check=True)
    

    result: CompletedProcess = subprocess.run(
        ["git", "show", "origin/{branch}:etc/version.json"],
        stdout=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        return "unknown"
    return json.loads(result.stdout)["version"]

def get_local_branch() -> str | None:
    result: CompletedProcess = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        stdout=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip()
    

def get_local_version() -> str:
    with open("etc/version.json", "r") as fp:
        return json.load(fp=fp)["version"]
    
def main() -> None:
    question: str | None = popup(title="Update Checker", message=f"An update has been found for charter: {get_local_version()} (local) vs {get_ref_version(get_local_branch() if get_local_branch() is not None else 'main')} (remote)\n\nWould you like to download it now? Selecting 'No' will continue to the currently installed version.", icon="info", options="yesnocancel")
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
    