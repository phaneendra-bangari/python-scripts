#This python script checks if a path is valid or not and tells us if the path is a file or a directory.
import os
INPUT_PATH=input("Enter a path to check if its FILE or DIRECTORY: ")
if os.path.exists(INPUT_PATH):
    print(f"The given Path: {INPUT_PATH} is a valid.")
    if os.path.isfile(INPUT_PATH):
        print(f"The given Path: {INPUT_PATH} is a file and the file name is {os.path.basename(INPUT_PATH)}")
    else: 
        print(f"The given Path: {INPUT_PATH} is a directory and the directory name is {os.path.dirname(INPUT_PATH)}")
else:
    print(f"The given Path: {INPUT_PATH} is a not valid.")

