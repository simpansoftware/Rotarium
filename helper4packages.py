import requests
import platform
import sys
import json

def search(package):
    r = requests.get(f"https://raw.githubusercontent.com/simpansoftware/rotarium-repo/refs/heads/main/{platform.system()}.txt")
    print("available packages:")
    packages = [i for i in r.text.splitlines() if package.lower() in i.lower()]
    if packages:
        for i in packages:
            print(i)
    else:
        print("uhh no packages are here i guess?")

    return packages

def install(package):
    r = requests.get(f"https://raw.githubusercontent.com/simpansoftware/rotarium-repo/refs/heads/main/{platform.system()}.txt")
    packages = [i.strip().lower() for i in r.text.splitlines()]
    if package.lower() in packages:
        r = requests.get(f"https://raw.githubusercontent.com/simpansoftware/rotarium-repo/refs/heads/main/{platform.system()}/{package.lower()}.py")
        print(f"do you want to install {package}?")
        thing = input("y/N")
        if thing.lower() == "y":
            exec(r.text)
        else:
            print("okay ba bye")
    else:
        print("specified package does not exist")

def register_package(package, binary_path, package_dir=None):
    try:
        with open("packages.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    data[package] = {
        "binary": binary_path,
        "dir": package_dir
    }
    
    with open("packages.json", "w") as f:
        json.dump(data, f, indent=4)

# why did i spend 30 minutes debugging just to forget this :sob:
if __name__ == "__main__":
    if len(sys.argv) >= 3:
        install(sys.argv[2])