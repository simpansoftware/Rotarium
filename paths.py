# this file was made by claude i assume with changes made by me

import shutil
import sys
from pathlib import Path

def appdir():
    path = Path.home() / ".rotarium"
    path.mkdir(parents=True, exist_ok=True)
    return path


def packageroot():
    return appdir() / "packages"


def jsonpath():
    return appdir() / "packages.json"


def venvpath():
    if sys.platform.startswith("win"):
        return packageroot() / "venv" / "Scripts" / "python.exe"
    return packageroot() / "venv" / "bin" / "python"


def syspy():
    candidates = []
    if sys.platform.startswith("win"):
        candidates = [["py", "-3"], ["python"], ["python3"]]
    else:
        candidates = [["python3"], ["python"]]

    for candidate in candidates:
        if shutil.which(candidate[0]):
            return candidate

    return None