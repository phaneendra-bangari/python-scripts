#Filter the files with .py ,txt extensions.
import os
'''
INPUT_DIRECTORY=input("Please enter the directory in which you want to segeregate the file types: ")
if os.path.isdir(INPUT_DIRECTORY) and os.path.exists(INPUT_DIRECTORY):
    print("This is a valid directory")
    INPUT_DIRECTORY_LIST=os.listdir(INPUT_DIRECTORY)
    for EACH_DIR_FILE in INPUT_DIRECTORY_LIST:
        if EACH_DIR_FILE.endswith(".py"):
            print(f"The file: {os.path.join(INPUT_DIRECTORY,EACH_DIR_FILE)} is a Python File")
        elif EACH_DIR_FILE.endswith(".sh"):
            print(f"The file: {os.path.join(INPUT_DIRECTORY,EACH_DIR_FILE)} is a Shell File")
        elif EACH_DIR_FILE.endswith(".txt"):
            print(f"The file: {os.path.join(INPUT_DIRECTORY,EACH_DIR_FILE)} is a Text File")
        elif EACH_DIR_FILE.endswith(".log"):
            print(f"The file: {os.path.join(INPUT_DIRECTORY,EACH_DIR_FILE)} is a Log File")
        elif os.path.isdir(os.path.join(INPUT_DIRECTORY,EACH_DIR_FILE)):
            print(f"The file: {os.path.join(INPUT_DIRECTORY,EACH_DIR_FILE)} is a Directory File")
        else:
            print(f"Could not identify the type of file for {os.path.join(INPUT_DIRECTORY,EACH_DIR_FILE)}")
else:
    print("This is not a valid path. Please enter a valid directory path.")
'''
INPUT_DIRECTORY=input("Please enter the directory in which you want to segeregate the file types: ")
if os.path.isdir(INPUT_DIRECTORY) and os.path.exists(INPUT_DIRECTORY):
    print("This is a valid directory")
    INPUT_DIRECTORY_LIST=os.listdir(INPUT_DIRECTORY)
    if len(INPUT_DIRECTORY_LIST) == 0:
        print("This is an empty directory")
    else:
        INPUT_EXTENSION_FILE=input("Enter the extension of the file which you want (.py, .sh, .txt, .log): ")
        NUMBER_OF_FILES_FOUND=0
        for EACH_DIR_FILE in INPUT_DIRECTORY_LIST:
            if EACH_DIR_FILE.endswith(INPUT_EXTENSION_FILE):
                print(f"File with {INPUT_EXTENSION_FILE} in given directory: {INPUT_DIRECTORY} is {os.path.join(INPUT_DIRECTORY,EACH_DIR_FILE)}")
                NUMBER_OF_FILES_FOUND=NUMBER_OF_FILES_FOUND+1
        print(f"Total number of files found: {NUMBER_OF_FILES_FOUND}")
else:
    print("This is not a valid path. Please enter a valid directory path.")

