# this file was made by claude i assume with changes made by me

import shutil
import sys
import subprocess
from pathlib import Path

def appdir():
    path = Path.home() / ".rotarium"
    path.mkdir(parents=True, exist_ok=True)
    return path

def validpython(cmd):
    try:
        result = subprocess.run(cmd + ["-c", "import sys; print(sys.executable)"], capture_output=True, text=True, timeout=2)
        path = result.stdout.strip()

        if not path:
            return False

        if "WindowsApps" in path:
            return False
        
        return True

    except Exception:
        return False

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

    for cmd in candidates:
        if shutil.which(cmd[0]) and validpython(cmd):
            return cmd

    return None
