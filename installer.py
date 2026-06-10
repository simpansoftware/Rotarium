import subprocess
import sys
import time
import platform
from pathlib import Path
import helper

def regularinstall():
    install = input("do you want to install Rotarium? y/N ")
    if install.lower() in ("y", "yes"):
        installrotarium()
    else:
        print("okay bye!")
        sys.exit()

def installrotarium():
    with open("packages.json", "w") as f:
        f.write("{}")
    Path("packages").mkdir(parents=True, exist_ok=True)   
    if platform.system() == "Linux":
        Path("packages/linux").mkdir(parents=True, exist_ok=True)
    else:
        Path("packages/windows").mkdir(parents=True, exist_ok=True)      
    result = subprocess.run([sys.executable, "-m", "venv", "packages/venv"])
    if result.returncode != 0:
        print("venv creation failed, install the dependencies i told you install and be happy, exiting...")
        sys.exit()
    helper.install_package("wedonottalkaboutrequeststhisishighlyneededforsetupifyouinstallthisyourrotariumwillbreakthatisnotonme")
    with open("packages.json", "w") as f:
        f.write("{}")
    with open("repos.txt", "w") as f:
        f.write("https://simpansoftware.cc/rotarium-repo/")
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