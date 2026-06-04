import sys

print("Rotarium\n")
if len(sys.argv) < 2:
    print("looks like you didnt pass an argument!\nuh oh, help is on the way!\nso like uhh\npython rotarium.py install and then whatever package to install i guess\npython rotarium.py remove and then whatever package to delete")
    sys.exit()
arg = sys.argv[1]

if arg == "install":
    print("stub")
elif arg == "remove":
    print("stub")
elif arg == "help":
    print("looks like you didnt pass an argument!\nuh oh, help is on the way!\nso like uhh\npython rotarium.py install and then whatever package to install i guess\npython rotarium.py remove and then whatever package to delete")
else:
    print("looks like you passed an illegal argument!\nuh oh, help is on the way!\nso like uhh\npython rotarium.py install and then whatever package to install i guess\npython rotarium.py remove and then whatever package to delete")