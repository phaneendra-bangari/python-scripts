# This script will check a given directory and lists all the directorys and files.

import os
import sys
INPUT_DIRECTORY=input("Please enter a directory path to check all the files and directories in that path: ")
if os.path.exists(INPUT_DIRECTORY) and os.path.isdir(INPUT_DIRECTORY):
    print(f"The path: {INPUT_DIRECTORY} is a valid path.")
else:
    print(f"The path: {INPUT_DIRECTORY} is an invalid path or not a directory path. Please provide the correct existing path.")
    sys.exit()

INPUT_DIRECTORY_LIST=os.listdir(INPUT_DIRECTORY)
for EACH_FILE in INPUT_DIRECTORY_LIST:
    if os.path.isfile(os.path.join(INPUT_DIRECTORY,EACH_FILE)):
        print(f"The path: {os.path.join(INPUT_DIRECTORY,EACH_FILE)} is a file.")
    else:
        print(f"The path: {os.path.join(INPUT_DIRECTORY,EACH_FILE)} is a directory.")


