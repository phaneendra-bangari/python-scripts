#Some basic OS PATH MODULE functions and variables.
import os
print(f"The OS Path Module Seperator is: {os.path.sep}")
print(f"To display only the file name of a path we can use basename(). The result is: {os.path.basename('/home/ec2-user/Scripts/python-scripts/README.md')}")
print(f"To display only the directory of the given file path, dirname() can be used. The result is: {os.path.dirname('/home/ec2-user/Scripts/python-scripts/README.md')}")
print(f"Joining the paths: /home/ec2-user/ and /Scripts/python-scripts using join(). The result is: {os.path.join('/home/ec2-user','Scripts/python-scripts')}")
print(f"Using split() for spliting the path /home/ec2-user/Scripts/python-scripts/README.md with basename and dirname: {os.path.split('/home/ec2-user/Scripts/python-scripts/README.md')}")
print(f"Size of the file /home/ec2-user/Scripts/python-scripts/README.md using getsize() is: {os.path.getsize('/home/ec2-user/Scripts/python-scripts/README.md')} bytes")
print(f"Is the file /home/ec2-user/Scripts/python-scripts/README.md exists? Result: {os.path.exists('/home/ec2-user/Scripts/python-scripts/README.md')}")
print(f"Is the path /home/ec2-user/Scripts/python-scripts/README.md a file? Result: {os.path.isfile('/home/ec2-user/Scripts/python-scripts/README.md')}")
print(f"Is the path /home/ec2-user/Scripts/python-scripts/README.md a directory? Result: {os.path.isdir('/home/ec2-user/Scripts/python-scripts/README.md')}")
print(f"Is the path /home/ec2-user/Scripts/python-scripts/readmelink a link? Result: {os.path.islink('/home/ec2-user/Scripts/python-scripts/readmelink')}")
