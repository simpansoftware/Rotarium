import requests
import platform

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