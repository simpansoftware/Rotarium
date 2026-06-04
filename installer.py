import subprocess
import sys
import time
import platform
from pathlib import Path

print("Rotarium Installer")
time.sleep(2)
if platform.system() in ("Linux", "Darwin", "Windows"):
    install = input("Do you want to install Rotarium? y/N ")
    if install.lower() in ("y", "yes"):
        with open(".installed", "w") as f:
            f.write("")
        Path("packages").mkdir(parents=True, exist_ok=True)    
        subprocess.run([sys.executable, "-m", "venv", "packages/venv"])
        print("installed! have a nice day!")
    else:
        print("okay bye!")
        sys.exit()
else:
    print(f"Unsupported OS: {platform.system()}, have a nice day!")