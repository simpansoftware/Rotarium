import subprocess
import sys
import time
import platform
from pathlib import Path
import helper
import shutil
import paths

def regularinstall():
    install = input("do you want to install Rotarium? y/N ")
    if install.lower() in ("y", "yes"):
        installrotarium()
    else:
        print("okay bye!")
        sys.exit()

def installrotarium():
    with open(paths.jsonpath(), "w") as f:
        f.write("{}")
    Path(paths.packageroot()).mkdir(parents=True, exist_ok=True)   
    if platform.system() == "Linux":
        Path(f"{paths.packageroot()}/linux").mkdir(parents=True, exist_ok=True)
    else:
        Path(f"{paths.packageroot()}/windows").mkdir(parents=True, exist_ok=True)     
    launcher = paths.syspy()
    if not launcher and platform.system() == "Windows" and shutil.which("winget"):
        print("python not found, attempting install with winget")
        result = subprocess.run(["winget", "install", "-e", "--id", "Python.Python.3.13", "--silent"])
        if result.returncode == 0:
            print("restart your console and rerun the installer please")
            sys.exit(0)
        else:
            print("python failed to install, try installing it manually")
            sys.exit(1)
    
    if not launcher:
        print("python not found, install it (and if you are on linux, make sure to install a version with venv support), then rerun the installer")
        sys.exit(1)

    result = subprocess.run([*launcher, "-m", "venv", f"{paths.packageroot()}/venv"])
    if result.returncode != 0:
        print("venv creation failed, install the dependencies i told you install and be happy, exiting...")
        sys.exit()
    helper.install_package("python-requests")
    with open(paths.jsonpath(), "w") as f:
        f.write("{}")
    print("installed! have a nice day!")

print("Rotarium Installer")
time.sleep(2)
if platform.system() in ("Linux", "Windows"):
    if platform.system() == "Linux":
        if platform.libc_ver()[0] != "glibc":
            print("glibc not detected, packages may not work properly")
            install = input("do you want to install Rotarium? (if you aren't completely sure you have glibc, say no!) y/N ")
            if install.lower() in ("y", "yes"):
                installrotarium()
            else:
                print("okay bye!")
                sys.exit()
        else:
            regularinstall()
    else:
        regularinstall()
else:
    print(f"unsupported OS: {platform.system()}, have a nice day!")