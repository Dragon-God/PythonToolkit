#! python3
#   Regex Search: Finds all lines matching a given regex in each file in a given folder.
#   Usage:
#       The directory to search is provided as a command line argument.
#       Script prompts the user to enter the regex.
#       After completion, the user is prompted to continue.

import re
from os import path, listdir

def extend(parent, *lst):
    for dct in lst:  parent.update(dct)

def regexSearch(regex, directory):
    res, lst = {}, listdir(directory)
    for itm in lst:
        pth = path.join(path.abspath(directory), itm)
        if path.isdir(pth):   extend(res, regexSearch(regex, pth))    #Recursively traverse all sub directories.
        else:
            print(pth)
            with open(pth) as file:  
                tmp = []
                for idx, line in enumerate(file.readlines()):
                    results = regex.findall(line)
                    if results:  tmp.extend([f"Line {idx+1}: {results}"])
                extend(res, {pth: tmp})
    return res

def main():
    while True:
        print("Input the name of the directory you want to search in:", end = "\t")
        directory = input()
        while not path.isdir(directory):
            print("Error: Please input a valid path for an existing directory:", end = "\t")
            directory = input()
        print("Input the name of the pattern you want to search for:", end = "\t")
        while True:
            try:
                pattern = input()
                regex = re.compile(pattern)
                break
            except TypeError:  print("Error: Please input a valid regex:", end = "\t")
            except re.error:  print("Error: Please input a valid regex:", end = "\t")
        matches = regexSearch(regex, directory)
        for key in matches:  print(key, "\n".join(matches[key]), sep="\n", end="\n\n")
        print("Do you want to continue? (Y/N):", end="\t")
        check = input().lower()
        if check not in {"y", "yes"}:  break

main()
