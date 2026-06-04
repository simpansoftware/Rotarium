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
            if platform.system() in ("Linux", "Darwin"):
                print("installing:", package)
                subprocess.run(["packages/venv/bin/python", "-m", "pip", "install", thing])
            else:
                print("installing:", package)
                subprocess.run(["packages/venv/Scripts/python.exe", "-m", "pip", "install", thing])
            with open(".installed", "a") as f:
                f.write(f"{package}\n")
        else:
            print("yeah no im doing this later")

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
            return package in [line.strip() for line in f]
    except FileNotFoundError:
        return False
    
def uninstall(package):
    