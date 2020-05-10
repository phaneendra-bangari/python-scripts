# Usage of Join, Center, Zfill, Strip, Split, Count, Index, Find, on Strings in Python
MY_NAME='Phaneendra Bangari'
MY_MOBILE_NUMBER='9550328609'
MY_CITY='Hyderabad, India.'

# Use of Join - It seperates a string with the mentioned characters.
print(f"Join Functions on Strings\n")
print(f"Joining my Mobile Number with space {' '.join(MY_MOBILE_NUMBER)}")
print(f"Joining my Mobile Number with asterick {'*'.join(MY_MOBILE_NUMBER)}")
print(f"Joining my Mobile Number with tab space");print("\t".join(MY_MOBILE_NUMBER))

print(f"\nCenter Functions on Strings\n")
# Use of Center - It centers the string with the mentioned space on the terminal output.
print(f"Below are the details with center format \n{MY_NAME.center(30)}\n{MY_CITY.center(30)}")

# Zfill - Padding - This fills the desired characters in a string.
print(f"\nZ - fill Functions on Strings\n")
NATIONAL_PHONE_NUMBER=MY_MOBILE_NUMBER.zfill(11)
print(NATIONAL_PHONE_NUMBER.center(30))

# Strip operations. We can remove a set of characters from a string. By default it removes a space in a string.
print(f"\nStrip Functions on Strings\n")
#Removing spaces in the starting or ending of the string.
print(f"Removing spaces from the sting using strip operations {MY_NAME.strip()}")

#Removing a character (.) from the starting or ending of a string.
print(f"Removing the special characters from the address string {MY_CITY.strip('.')}")
print(f"Removing number 9 from starting and ending of {MY_MOBILE_NUMBER} results to {MY_MOBILE_NUMBER.strip('9')}")

# lstrip is the strip performed only from the left side. Similarly we have rstrip which strips only the right of the string.
print(f"Removing the first 9 only from {MY_MOBILE_NUMBER} results to {MY_MOBILE_NUMBER.lstrip('9')}")

# Using multiple strip on the same string
print(f"Shortening India to Ind: {MY_CITY.rstrip('.').strip('ia').upper()}")

print(f"\nSplit Functions on Strings\n")
#Split Operations on Strings. By default the split will be done by a space.
print(f"Spliting a string with space operations {MY_NAME.split()}")
print(f"Spliting a string with a character 0 results in {MY_MOBILE_NUMBER.split('0')}")

print(f"\nCount Functions on Strings\n")

# Count Operations on Strings
print(f"Count of a character \'a\' in {MY_NAME} is {MY_NAME.count('a')}")
print(f"Count of the word \'an\' in {MY_NAME} is {MY_NAME.count('an')}")
print(f"Count of spaces in {MY_NAME} is {MY_NAME.count(' ')}")

print(f"\nIndex Functions on Strings\n")

# Index Operations - It returns the first index of the characters as input.
print(f"Index of the first \'P\' in {MY_NAME} is {MY_NAME.index('P')}") #If P is not found, it returns error.
print(f"Index of the character \'a\' but not the third index in {MY_NAME} is {MY_NAME.index('a',3)}")

print(f"\nFind Functions on Strings\n")
#Find Function on Strings - Returns -1 if not found. Returns the first character index value if found.
print(f"Finding the string \'Bangari\' in {MY_NAME}, it starts at the Index {MY_NAME.find('Bangari')}")
print(f"Finding for the character which is not there in {MY_NAME} to see if I get {MY_NAME.find('K')}") #-1 should be returned.

#Similarly you can ignore the first found index by traversing to further indexes.
print(f"Ignoring the first index of \'a\' in {MY_NAME} results with the next index value as {MY_NAME.find('a',3)}")
