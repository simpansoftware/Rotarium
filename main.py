import sys
import helper

print("Rotarium\n")
helptext = """usage:
    python main.py install <package>
    python main.py remove <package>
    python main.py run <package>
    python main.py pyrun <python script> 
    python main.py help"""

if len(sys.argv) < 2:
    print(helptext)
    sys.exit()

arg = sys.argv[1]
if arg == "install":
    if len(sys.argv) < 3:
        print("you didnt specify a package")
    else:
        helper.install(sys.argv[2])
        print("done!")
elif arg == "remove":
    print("stub")
elif arg == "run":
    helper.run(sys.argv[2], sys.argv[3:])
elif arg == "pyrun":
    print("stub")
elif arg == "help":
    print(helptext)
else:
    print(helptext)