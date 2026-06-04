import subprocess
import platform

def get_venv():
    if platform.system() in ("Linux", "Darwin"):
        return "packages/venv/bin/python"
    else:
        return "packages/venv/Scripts/python.exe"
        
def install_package(package):
    if package.startswith("python-"):
        if platform.system() in ("Linux", "Darwin"):
            subprocess.run(["packages/venv/bin/python", "-m", "pip", "install", package])
        else:
            subprocess.run(["packages/venv/Scripts/python.exe", "-m", "pip", "install", package])
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