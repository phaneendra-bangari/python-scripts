#Using some simple commands using sys module
from sys import *

#print(version)
#print(version_info)
#print(path)

#Script to do case convertion of given inputs.

if len(argv) != 3:
    print("Please enter atleast 2 inputs for the script to execute")
    exit()

USER_STRING=argv[1]
USER_ACTION=argv[2]

if USER_ACTION == 'lower':
    print(f"Given string in lower case is: {USER_STRING.lower()}")
elif USER_ACTION == 'upper':
    print(f"Given string in upper case is: {USER_STRING.upper()}")
elif USER_ACTION == 'title':
    print(f"Given string in title case is: {USER_STRING.title()}")
else:
    print("Please use the second string as title|lower|upper")

