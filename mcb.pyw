#! python3
#   mcb.pyw - Saves and loads pieces of text to the clipboard.
#   Usage: 
#       `mcb.pyw save <keyword>`    - Saves keyword to clipboard.
#       `mcb.pyw load <keyword>`    - Loads keyword to clipboard.
#       `mcb.pyw list`              - Loads all keywords to clipboard.


import shelve as sh, pyperclip as pypc, sys

pypc.copy("success")

with sh.open("mcb") as shelf:
    args = sys.argv
    pypc.copy(str(args))
    #ToDo:  Save clipboard content.
    if args[1].lower() == "save": 
        if args[2] != "ALL":  shelf[args[2]] = pypc.paste()

    # #ToDo:  Load keyword to clipboard.
    elif args[1].lower() == "load": pypc.copy(shelf[args[2]])

    # #ToDo:  List all keywords.
    elif args[1].lower() == "list": pypc.copy(str(list(a for a in shelf)))

    elif args[1].lower() == "delete":
        del shelf[args[2]] if args[2] != "ALL" else shelf