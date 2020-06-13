#Copying content from one file to another file using read and writing files
import os
READ_SOURCE=input("Enter the source file to be copied: ")
READ_DEST=input("Enter the destination location to where the file to be copied: ")

if os.path.exists(READ_SOURCE) and os.path.isfile(READ_SOURCE):
    print("Entered file is correct and its a file.")
    if os.path.exists(READ_DEST) and os.path.isdir(READ_DEST):
        print("Entered destination is correct and its a destination type of file.")
        READ_FILE=open(READ_SOURCE,'r')
        SOURCE_CONTENT=READ_FILE.read()
        READ_FILE.close()
        WRITE_FILE_NAME=os.path.join(READ_DEST,os.path.basename(READ_SOURCE))
        WRITE_FILE=open(WRITE_FILE_NAME,'w')
        WRITE_FILE.write(SOURCE_CONTENT)
        WRITE_FILE.close()
        print("File copied successfully")
    else:
        print("Entered destination is not correct. Give a directory path.")
else:
    print("Invalid Source File. Enter a valid source path.")
