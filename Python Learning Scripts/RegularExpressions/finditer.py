#This returns the memory object location by default. Its same as the findall operation.
import re
TEST_STRING="I installed Python on my OS. Python2 is older version. Python3 is newer version."
PATTERN=r'\bPython[23]?\b'
print(re.finditer(PATTERN,TEST_STRING)) #This returns the memory object location of this.

#Accessin the object using for loop.
for ACCESS_OBJ in re.finditer(PATTERN,TEST_STRING):
    print("The pattern searched is", ACCESS_OBJ.group())
    print("The start index is", ACCESS_OBJ.start())
    print("The ending index is", ACCESS_OBJ.end())

