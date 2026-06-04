import sys

print("Rotarium\n")
helptext = """
usage:
    python main.py install <package>
    python main.py remove <package>
    python main.py help
"""
if len(sys.argv) < 2:
    print(helptext)
    sys.exit()
arg = sys.argv[1]


if arg == "install":
    print("stub")
elif arg == "remove":
    print("stub")
elif arg == "help":
    print(helptext)
else:
    print(helptext)