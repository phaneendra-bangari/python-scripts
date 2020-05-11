'''
Dictionary Data types follows Key-value representations
Access the values with the Key using the function "get"
To display only Keys of a Dictionary data, use the keys function.
To display only Values of a Dictionary data, use the values function.
'''

# Dictionary data declaration
MY_EATABLES={"Fruits":"Mango","Vegetables":"Tomato","Sweets":"Laddu","Breakfast":"Dosa"}
MY_EATABLES_NEW={"Lunch":"Rice","Dinner":"Chapathi"}
MY_TOOLS={"Python":3,"Java":11}

# Accessing the values using keys using get function on Dictionary Data Types
print(f"My favourite Vegetables from MY_EATABLES is {MY_EATABLES.get('Vegetables')}")
print(f"My favourite Dinner from MY_EATABLES is {MY_EATABLES.get('Dinner')}") # Accessing this way leads to "None" value. If you access using MY_EATABLES["Dinner"] will throw an error.

# Accessing all the Key's of a Dictionary.
print(f"All the declared Key\'s in MY_EATABLES is {MY_EATABLES.keys()}")

#Accessing all the Values of a Dictionary.
print(f"All the declared Value\'s in MY_EATABLES is {MY_EATABLES.values()}")

# Adding more content to the Dictionary.
MY_EATABLES["Snacks"]="Pani Puri" # Adds this data at the end of the MY_EATABLES Dictionary.
print(f"Data in MY_EATABLES after adding Snacks into it is {MY_EATABLES}")

# Copy function on Dictionaries.
MY_EATABLES_BACKUP=MY_EATABLES.copy() # Be aware that copy functions uses a different memory location.
print(f"Backup copy of MY_EATABLES variable is MY_EATABLES_BACKUP: {MY_EATABLES_BACKUP}")

# Adding new Dictionary to present Dictionary using update function. This appends the new content to present Dictionary.
MY_EATABLES.update(MY_EATABLES_NEW)
print(f"Adding MY_EATABLES_NEW to MY_EATABLES using update() function results as {MY_EATABLES}")

# pop function removes the Dictionary key-value pair using the key as input.
MY_EATABLES.pop("Lunch") # pop() always needs a key to be removed.
print(f"After removing Lunch from MY_EATABLES using pop() function results are {MY_EATABLES}")

# popitem() removes the key-value pair randomly. It dont require any input.

# Items functions on Dictionaries.
MY_TOOLS.items()
print(f"MY_TOOLS content after using the items() function is {MY_TOOLS}")

# Fromkeys - Using this function, you can create a Dictionary from list as input to this function.
FIRST_NAMES_LIST=["Phaneendra","Teja","Swaroop"]
EMPLOYEE_DETAILS_DIC=dict.fromkeys(FIRST_NAMES_LIST) # Use the dict.fromkeys() to convert to Dictionary data type.
print(f"After adding Keys from FIRST_NAMES_LIST to EMPLOYEE_DETAILS_DIC the values of EMPLOYEE_DETAILS_DIC are {EMPLOYEE_DETAILS_DIC}")

# setdefault - Using the default value to the keys which dont have any value.
EMPLOYEE_DETAILS_DIC.setdefault("Phaneendra","Devops Engineer")
print(f"After setting the default value for a key - Phaneendra in EMPLOYEE_DETAILS_DIC the result is {EMPLOYEE_DETAILS_DIC}") # Observe that the value is "None". If a value already exists (this case None) this function wont change.
EMPLOYEE_DETAILS_DIC.setdefault("Kiran","Network Engineer")
print(f"After setting the default value for a new key - Kiran in EMPLOYEE_DETAILS_DIC the result is {EMPLOYEE_DETAILS_DIC}")

'''
SETS Data Types
SETS are unorderd data.
SETS ignore the duplicate data.
'''
MYSETS_STOCK_AN_HOUR={1,2,7,7.9,4.5,4,19,10,7,1}
print(f"The values of MYSETS_STOCK_AN_HOUR is {MYSETS_STOCK_AN_HOUR} and its type is {type(MYSETS_STOCK_AN_HOUR)}") # You get the UNIQUE data and unorderd data, not like how we represented.


# Converting a list to SETS
TEMPORARY_LIST=[1,2,7,7.9,4.5,4,19,10,7,1]
SETS_TEMPORATY_LIST=set(TEMPORARY_LIST)
print(f"After converting the data of lists TEMPORARY_LIST to sets SETS_TEMPORATY_LIST the SETS_TEMPORATY_LIST values are {SETS_TEMPORATY_LIST}")

# Perform UNION, INTERSECTIONS on SETS.
SETS_DATA_A={1,2,3,5,9}
SETS_DATA_B={5,1,4,10}
print(f"SETS_DATA_A UNION of SETS_DATA_B is {SETS_DATA_A.union(SETS_DATA_B)}")
print(f"SETS_DATA_A INTERSECTIONS of SETS_DATA_B is {SETS_DATA_A.intersection(SETS_DATA_B)}")

