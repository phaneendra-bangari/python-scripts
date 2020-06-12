#To find out files greater than X days in a given path.
import os
from datetime import datetime
INPUT_PATH=input("Enter a path where you need to find the files: ")

if os.path.isdir(INPUT_PATH) and os.path.exists(INPUT_PATH):
    print("Entered path is correct.")
    INPUT_DAYS=input("Enter howmany days older files you need: ")
    for EACH_FILE in os.listdir(INPUT_PATH):
        FILE_NAME_AND_PATH=os.path.join(INPUT_PATH,EACH_FILE)
        FILE_CREATED_DAYS_BACK=(datetime.now()-datetime.fromtimestamp(os.path.getctime(FILE_NAME_AND_PATH))).days
        if int(FILE_CREATED_DAYS_BACK) >= int(INPUT_DAYS):
            print(f"{FILE_NAME_AND_PATH} is changed {FILE_CREATED_DAYS_BACK} days back.")
else:
    print("Invalid path or the path is a file. Please give a directory.")
