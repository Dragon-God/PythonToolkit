#! python3
#   `regexSearch`: Finds all lines matching a given regex in each file in a given folder.
#   Usage:
#       The directory to search and regex to be searched for are provided as a command line arguments.
#       The 1st and 2nd command line arguments are the directory and regex pattern respectively.
#       Script prompts the user to enter the regex.
#       After completion, the user is prompted to continue

import re, sys
from os import path, listdir

def regex_search(regex, directory):
    res, lst = {}, listdir(directory)
    for itm in lst:
        pth = path.join(path.abspath(directory), itm)
        if path.isdir(pth):   res.update(regex_search(regex, pth))    #Recursively traverse all sub directories.
        else:
            print(pth)
            with open(pth) as file:  
                tmp = []
                for idx, line in enumerate(file.readlines()):
                    results = regex.findall(line)
                    if results:  tmp.extend([f"Line {idx+1}: {results}"])
                res[pth] = tmp
    return res

if __name__ == "__main__":
    directory, pattern = sys.argv[1:3]
    while not path.isdir(directory):
        print("Error: Please input a valid path for an existing directory:", end = "\t")
        directory = input()
    while True:
        try:
            regex = re.compile(pattern)
            break
        except TypeError:
            print("Error: Please input a valid regex:", end = "\t")
            pattern = input()
        except re.error:
            print("Error: Please input a valid regex:", end = "\t")
            pattern = input()
    matches = regex_search(regex, directory)
    for key in matches:  print(key, "\n".join(matches[key]), sep="\n", end="\n\n")
