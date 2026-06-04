import subprocess
import sys
import time
import platform

print("Rotarium Installer")
time.sleep(2)
if platform in ("Linux", "Darwin", "Windows"):
    install = input("Do you want to install? y/N")
    if install == "y":
        with open(".installed", "w") as f:
            f.write("")
        subprocess.run(["python", "-m", "venv", "venv"])
        print("installed! have a nice day!")
    else:
        print("okay bye!")
        sys.exit
else:
    print("Unsupported OS, have a nice day!")