import sys
import install

print("Rotarium\n")
helptext = """usage:
    python main.py install <package>
    python main.py remove <package>
    python main.py run <package>
    python main.py help"""

if len(sys.argv) < 2:
    print(helptext)
    sys.exit()

arg = sys.argv[1]
if arg == "install":
    if len(sys.argv) < 3:
        print("you didnt specify a package")
    else:
        print("so uhh i forgot to implement this part, be right back!")
elif arg == "remove":
    print("stub")
elif arg == "run":
    print("stub")
elif arg == "help":
    print(helptext)
else:
    print(helptext)