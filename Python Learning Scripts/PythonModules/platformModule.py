#Some basic operations using Platform module in Python.
from platform import * # Importing the platform module.

#print(help("platform"))

print(f"Architecture of the current OS is: {architecture()}")
print(f"Machine type of the current OS is: {machine()}")
print(f"Node of the current OS is: {node()}")
print(f"Platform typeof the current OS is: {platform()}")
print(f"Processor of the current OS is: {processor()}")
print(f"Python Build of the current OS is: {python_build()}")
print(f"Release of the current OS is: {release()}")
print(f"UNAME of the current OS is: {uname()}")
print(f"System type of the current OS is: {system()}")
