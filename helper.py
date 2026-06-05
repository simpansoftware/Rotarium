import subprocess
import platform
import os
import json
import shutil

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
            result = subprocess.run([get_venv(), "-m", "pip", "install", thing])
        else:
            result = subprocess.run([get_venv(), os.path.abspath("helper4packages.py"), platform.system(), package])
        
        if result.returncode == 0:
            with open(".installed", "a") as f:
                f.write(f"{package}\n")
            print("done!")
        else:
            print("uhh something failed and i dont know what")

def run(thing, args=None):
    if args is None:
        args = []
    if thing.startswith("python-"):
        package = thing[len("python-"):]
        print(f"running {package}")
        subprocess.run([str(get_venv()), "-m", package, *args])
    else:
        with open("packages.json", "r") as f:
            data = json.load(f)
        if thing in data:
            subprocess.run([data[thing]["binary"], *args])
        else:
            print(f"{thing} isn't installed")

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
        else:
            try:
                with open("packages.json", "r") as f:
                    data = json.load(f)
                if package in data:
                    if data[package].get("dir"):
                        shutil.rmtree(data[package]["dir"])
                    else:
                        os.remove(data[package]["binary"])
                    del data[package]
                    with open("packages.json", "w") as f:
                        json.dump(data, f, indent=4)
            except FileNotFoundError:
                pass

        with open(".installed", "r") as f:
            linething = f.readlines()
        with open(".installed", "w") as f:
            for i in linething:
                if i.strip() != package:
                    f.write(i)
        print(f"uninstalled {package}")