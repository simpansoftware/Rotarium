import requests
import platform
import sys
import json
import hashlib

def search(package):
    r = requests.get(f"https://simpansoftware.cc/rotarium-repo/{platform.system()}.txt")
    print("available packages:")
    if package == "*":
        print(r.text)
    else:
        packages = [i for i in r.text.splitlines() if package.lower() in i.lower()]
        if packages:
            for i in packages:
                print(i)
        else:
            print("uhh no packages are here i guess?")

        return packages

def install(package):
    r = requests.get(f"https://simpansoftware.cc/rotarium-repo/{platform.system()}.txt")
    packages = [i.strip().lower() for i in r.text.splitlines()]
    if package.lower() in packages:
        r = requests.get(f"https://simpansoftware.cc/rotarium-repo/{platform.system()}/{package.lower()}.py")
        sha256 = requests.get(f"https://simpansoftware.cc/rotarium-repo/{platform.system()}/{package.lower()}.py.sha256")
        rbutraw = r.content
        sha256strip = sha256.text.strip()
        thingtwo = hashlib.sha256(rbutraw).hexdigest()
        print(thingtwo)
        if thingtwo != sha256strip:
            print("package has been tampered with, do not trust")
            return 1
        else:
            print(f"do you want to install {package}?")
            thing = input("y/N ")
            if thing.lower() == "y":
                exec(rbutraw.decode("utf-8"))
                return 0
            else:
                print("okay ba bye")
                return 2
    else:
        print("specified package does not exist")

def register_package(package, binary_path, package_dir=None):
    try:
        with open("packages.json", "r") as f:
            content = f.read()
            data = json.loads(content) if content.strip() else {}
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
        sys.exit(install(sys.argv[2]))