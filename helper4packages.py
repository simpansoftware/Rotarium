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
        r = requests.get(f"https://simpansoftware.cc/rotarium-repo/{platform.system()}/{package.lower()}/install.py")
        sha256 = requests.get(f"https://simpansoftware.cc/rotarium-repo/{platform.system()}/{package.lower()}/install.py.sha256")
        manifest = requests.get(f"https://simpansoftware.cc/rotarium-repo/{platform.system()}/{package.lower()}/manifest.json").json()
        required = ["package", "version", "info"]
        for bread in required: #because bread taste better than key
            if bread not in manifest:
                print("broken manifest")
                return 1
        rbutraw = r.content
        sha256strip = sha256.text.strip()
        if len(sha256strip) != 64:
            print("the hash didn't download correctly, please retry installation")
            return 1
        else:
            thingtwo = hashlib.sha256(rbutraw).hexdigest()
            if thingtwo != sha256strip:
                print("package has been tampered with (or is corrupt), please retry installation")
                return 1
            else:
                print(f"do you want to install {package}?")
                thing = input("y/N ")
                if thing.lower() == "y":
                    env = globals().copy()
                    env["manifest"] = manifest
                    exec(rbutraw.decode("utf-8"), env)
                    return 0
                else:
                    print("okay ba bye")
                    return 2
    else:
        print("specified package does not exist")

def register_package(package, binary_path, version, info, package_dir=None):
    try:
        with open("packages.json", "r") as f:
            content = f.read()
            data = json.loads(content) if content.strip() else {}
    except FileNotFoundError:
        data = {}
    
    data[package] = {
        "binary": binary_path,
        "dir": package_dir,
        "version": version,
        "info": info
    }
    
    with open("packages.json", "w") as f:
        json.dump(data, f, indent=4)

def manfetch(package):
    try:
        r = requests.get(f"https://simpansoftware.cc/rotarium-repo/{platform.system()}/{package.lower()}/manifest.json")
        r.raise_for_status()
        return r.json()
    except:
        return
    
def upgrade(package):
    import helper
    with open("packages.json", "r") as f:
        data = json.load()
    
    if not data:
        print("package not installed")
        return
    
    manifest = manfetch(package)
    if not manifest:
        print("failed to fetch manifest")
        return
    
    local = data.get("version")
    online = manifest.get("version")

    if local == online:
        print(f"{package} is up to date")
        return
    
    print(f"do you want to upgrade {package}? {local} -> {online}")
    text = input("backup config files and whatnot before this! y/N ")
    if text == "y".lower():
        helper.uninstall(package)
        helper.install_package(package)


# why did i spend 30 minutes debugging just to forget this :sob:
if __name__ == "__main__":
    if len(sys.argv) >= 3:
        sys.exit(install(sys.argv[2]))