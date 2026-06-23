import helper
import requests
import platform
import json
import paths

def manfetch(package):
    try:
        r = requests.get(f"https://simpansoftware.cc/rotarium-repo/{platform.system()}/{package.lower()}/manifest.json")
        r.raise_for_status()
        return r.json()
    except:
        return
    
def upgrade(package):
    with open(paths.jsonpath(), "r") as f:
        data = json.load(f)
    
    if package not in data:
        print("package not installed")
        return
    
    manifest = manfetch(package)
    if not manifest:
        print("failed to fetch manifest")
        return
    
    local = data[package]["version"]
    online = manifest.get("version")

    if local == online:
        print(f"{package} is up to date")
        return
    
    print(f"do you want to upgrade {package}? {local} -> {online}")
    text = input("backup config files and whatnot before this! y/N ")
    if text.lower() == "y":
        helper.uninstall(package)
        helper.install_package(package)