#Using the os module variables and functions.
import os
'''
print(f"The seperator in sep of os module is : {os.sep}")
print(f"The current working directory using getcwd function is: {os.getcwd()}")
print(f"Changing the current working director from {os.getcwd()} to /home/ec2-user/Scripts/python-scripting:")
os.chdir('/home/ec2-user/Scripts/python-scripts')
print(f"Current working directory is {os.getcwd()}")
print(f"Listing the current working directory {os.listdir()}")
print(f"Listing the content of /home/ec2-user/Scripts/python-scripts {os.listdir('/home/ec2-user/Scripts/python-scripts')}")
print(f"Creating the directory TemporaryDirectory at {os.getcwd()}")
#os.mkdir("TemporaryDirectory")
os.makedirs("/home/ec2-user/Scripts/python-scripts/AnotherTemporaryDirectory/InsideTemporaryDirectory")
print(f"Lising the current working directory after creating TemporaryDirectory: {os.listdir()}")
print(f"Lising the directory /home/ec2-user/Scripts/python-scripts/AnotherTemporaryDirectory/ after creating /home/ec2-user/Scripts/python-scripts/AnotherTemporaryDirectory/InsideTemporaryDirectory: {os.listdir('/home/ec2-user/Scripts/python-scripts/AnotherTemporaryDirectory/')}")

#print("Deleting the created directories")
# This command could be used for files deletion os.remove("Temporarary Files")
#os.removedirs("/home/ec2-user/Scripts/python-scripts/AnotherTemporaryDirectory/")
#print(f"Lising the current working directory after deleting TemporaryDirectory: {os.listdir()}")
#print(f"Lising the directory /home/ec2-user/Scripts/python-scripts/AnotherTemporaryDirectory/ after deleting /home/ec2-user/Scripts/python-scripts/AnotherTemporaryDirectory/InsideTemporaryDirectory: {os.listdir('/home/ec2-user/Scripts/python-scripts/AnotherTemporaryDirectory/')}")
'''
print(os.environ)
print(os.getuid())
print(os.getgid())
#os.rename(source,destination)

