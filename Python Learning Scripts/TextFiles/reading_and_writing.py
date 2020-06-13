#to create and modify existing files.

#General way to create file and write content in that.
FILE_OBJECT=open("newfile.py",'w') #If a file already exists, that file will be deleted and created a new one.
FILE_OBJECT.write("This is the first line. \n")
MY_CONTENT=["This is the first line from the list. \n","This is the second line from the list. \n"]
FILE_OBJECT.writelines(MY_CONTENT)
print(FILE_OBJECT.mode)
print(FILE_OBJECT.writable())
FILE_OBJECT.close()

#Using Loop and append format.
MY_CONTENT2=["This is first line of Content 2.","This is second line of Content 2.","This is third line of Content 3."]
FILE_OBJECT2=open("newfile.py","a")
for EACH_LIST in MY_CONTENT2:
    FILE_OBJECT2.write(EACH_LIST+"\n")
FILE_OBJECT2.close()

#Using the read format of the file.
FILE_OBJECT3_READ=open("newfile.py","r")
FILE_CONTENT=FILE_OBJECT3_READ.read() #This reads all the content fo the file and stores in FILE_CONTENT variable.
print(FILE_OBJECT3_READ.readable())
FILE_OBJECT3_READ.close()
print(FILE_CONTENT)

#Reading file content using for loop for the first 3 lines and the last line.
FILE_OBJECT_4_READ=open("newfile.py","r")
READ_FILE_4=FILE_OBJECT_4_READ.readlines()
FILE_OBJECT_4_READ.close()
for FILE_CONTENT_4 in range(3):
    print(READ_FILE_4[FILE_CONTENT_4])
print(READ_FILE_4[-1])

