#Understanding GETPASS MODULE
from getpass import *

print(f"You are logged in as {getuser()}") #This gets the user from the default env variables for the connected user.
PASSWORD=getpass(f"Enter the password for {getuser()}: ")
if PASSWORD == '1234567890':
    print("Authentication successful")
else:
    print("Authentication denied")

