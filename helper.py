import subprocess
import platform
import os
import json
import shutil
import helper4packages
import paths

def get_venv():
    return str(paths.venvpath())
        
def install_package(package):
    if is_installed(package):
        print(f"{package} is already installed")
        return
    
    if package.startswith("python-"):
        thing = package[len("python-"):]
        print("installing:", package)
        result = subprocess.run([get_venv(), "-m", "pip", "install", thing]).returncode
    else:
        result = helper4packages.install(package)
        if result is None:
            result = 1
    if result == 0:
        if package.startswith("python-"):
            register_pypackage(package)
        print("done!")
    elif result == 2:
        print("install aborted")
    else:
        print("uhh something failed and i dont know what")

#copied straight out of helper4packages with some json change
def register_pypackage(package):
    try:
        with open(paths.jsonpath(), "r") as f:
            content = f.read()
            data = json.loads(content) if content.strip() else {}
    except FileNotFoundError:
        data = {}
    
    data[package] = {
        "type": "python",
    }
    
    with open(paths.jsonpath(), "w") as f:
        json.dump(data, f, indent=4)

def run(thing, args=None):
    if args is None:
        args = []
    if thing.startswith("python-"):
        package = thing[len("python-"):]
        print(f"running {package}")
        subprocess.run([str(get_venv()), "-m", package, *args])
    else:
        with open(paths.jsonpath(), "r") as f:
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
    with open(paths.jsonpath(), "r") as f:
        shittyvariablename = json.load(f)
    return package in shittyvariablename
    
def uninstall(package):
    if not is_installed(package):
        print(f"{package} isn't installed")
        return
    else:
        data = {}
        if package.startswith("python-"):
            thing = package[len("python-"):]
            subprocess.run([get_venv(), "-m", "pip", "uninstall", "-y", thing])
            try:
                with open(paths.jsonpath(), "r") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = {}

            if package in data:
                del data[package]
                with open(paths.jsonpath(), "w") as f:
                    json.dump(data, f, indent=4)
        else:
            try:
                with open(paths.jsonpath(), "r") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = {}
            if package in data:
                if data[package].get("dir"):
                    shutil.rmtree(data[package]["dir"])
                else:
                    os.remove(data[package]["binary"])
                del data[package]
                with open(paths.jsonpath(), "w") as f:
                    json.dump(data, f, indent=4)

        print(f"uninstalled {package}")

def package_data(package):
    with open(paths.jsonpath(), "r") as f:
        data = json.load(f)
    return data.get(package)

def getver(package):
    data = package_data(package)
    if not data:
        print("package not installed")
        return
    print(data.get("version", "unknown"))

def getinfo(package):
    data = package_data(package)
    if not data:
        print("package not installed")
        return
    print(data.get("info", "no info available"))