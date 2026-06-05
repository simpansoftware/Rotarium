import subprocess
import platform
import os

def get_venv():
    if platform.system() in ("Linux", "Darwin"):
        return "packages/venv/bin/python"
    else:
        return "packages/venv/Scripts/python.exe"
        
def install_package(package):
    if is_installed(package):
        print(f"{package} is already installed")
        return
    else:
        if package.startswith("python-"):
            thing = package[len("python-"):]
            print("installing:", package)
            subprocess.run([get_venv(), "-m", "pip", "install", thing])
        else:
            pyrun(f"helper4packages.py {platform.system()} {package}")

def run(thing, args=None):
    if args is None:
        args = []
    if thing.startswith("python-"):
        package = thing[len("python-"):]
        print(f"running {package}")
        subprocess.run([str(get_venv()), "-m", package, *args])

    else:
        print("so uhh i forgot to do this part")

def pyrun(thing, args=None):
    if args is None:
        args = []

    subprocess.run([get_venv(), os.path.abspath(thing), *args])

def is_installed(package):
    try:
        with open(".installed", "r") as f:
            return package in [i.strip() for i in f]
    except FileNotFoundError:
        return False
    
def uninstall(package):
    if not is_installed(package):
        print(f"{package} isn't installed")
    else:
        if package.startswith("python-"):
            thing = package[len("python-"):]
            subprocess.run([get_venv(), "-m", "pip", "uninstall", "-y", thing])
            with open(".installed", "r") as f:
                linething = f.readlines()
            with open(".installed", "w") as f:
                for i in linething:
                    if i.strip() != package:
                        f.write(i)
            print(f"uninstalled {package}")
        else:
            print("remind me to implement this later")