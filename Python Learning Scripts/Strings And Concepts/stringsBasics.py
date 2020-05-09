# I am writing this learning script from Atom Windows Office Laptop

# Double Colon Variable Declaration
my_name="Phaneendra K"

# Single Colon Variable Declaration
my_lastname='Bangari'

# Multiline Variable Declaration.
my_info='''I am learning Python Scripting.
This is along with GIT & GITHUB
'''

# Slicing of Strings - Accessing Variable Indexes
print(f"This is the first character of {my_name} is {my_name[0]}")
print(f"This is the last character of {my_lastname} is {my_lastname[-1]}")

# Accessing Variable Indexes and printing a part of the string.
print(f"This is the first name of {my_name} is {my_name[0:10]}")

# Predefined Functions on Strings
print(f'Length of {my_lastname} is {len(my_lastname)}')

#Concatenation of two Strings
my_fullname=my_name+" "+my_lastname
print(f'Full Name is {my_fullname}')
