import sys
import helper
import helper4packages
import json

print("Rotarium\n")
helptext = """usage:
    python main.py install <package> - installs a package
    python main.py remove <package> - uninstalls an installed package
    python main.py upgrade <package> - upgrades an installed package
    python main.py run <package> - runs an installed package
    python main.py pyrun <python script> - runs a python script with the rotarium venv
    python main.py search <package> - searches for a package, search * to see all packages, on linux PLEASE quote the star
    python main.py help - displays this message
    python main.py list - lists installed packages
    python main.py version <package> - gets version of installed package
    python main.py info <package> - gets info of installed package"""

if len(sys.argv) < 2:
    print(helptext)
    sys.exit()

arg = sys.argv[1]
if arg == "install":
    if len(sys.argv) < 3:
        print("you didnt specify a package")
    else:
        helper.install_package(sys.argv[2])
elif arg == "remove":
    helper.uninstall(sys.argv[2])
elif arg == "run":
    helper.run(sys.argv[2], sys.argv[3:])
elif arg == "pyrun":
    helper.pyrun(sys.argv[2], sys.argv[3:])
elif arg == "help":
    print(helptext)
elif arg == "list":
    print("installed packages:")
    with open("packages.json", "r") as f:
        data = json.load(f)
    if not data:
        print("no packages installed")
    else:
        for i in data:
            print(i)
elif arg == "search":
    helper4packages.search(sys.argv[2])
elif arg == "version":
    if len(sys.argv) < 3:
        print("specify a package next time, kay?")
    else:
        helper.getver(sys.argv[2])
elif arg == "info":
    if len(sys.argv) < 3:
        print("specify a package next time, kay?")
    else:
        helper.getinfo(sys.argv[2])
elif arg == "upgrade":
    if len(sys.argv) < 3:
        print("specify a package next time, kay?")
    else:
        helper4packages.upgrade(sys.argv[2])
else:
    print(helptext)