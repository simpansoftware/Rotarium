import subprocess
import sys
import time
import platform
from pathlib import Path
import helper

print("Rotarium Installer")
time.sleep(2)
if platform.system() in ("Linux", "Windows"):
    install = input("do you want to install Rotarium? y/N ")
    if install.lower() in ("y", "yes"):
        with open(".installed", "w") as f:
            f.write("")
        Path("packages").mkdir(parents=True, exist_ok=True)   
        if platform.system() == "Linux":
            Path("packages/linux").mkdir(parents=True, exist_ok=True)
        else:
            Path("packages/windows").mkdir(parents=True, exist_ok=True)      
        subprocess.run([sys.executable, "-m", "venv", "packages/venv"])
        helper.install_package("python-requests")
        print("installed! have a nice day!")
    else:
        print("okay bye!")
        sys.exit()
else:
    print(f"unsupported OS: {platform.system()}, have a nice day!")