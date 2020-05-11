'''
Lists are a data types used in Python to store different data forms together.
Empty list results boolean false while type conversion.
Lists are mutable, and hence they can be modified.
Use "dir" to get more details on the list operations.
'''
# Declaring Variables.
MY_FRIENDS=["Teja","Swaroop","Kiran"]
MY_LUCKY_NUMBERS=[3,7,12,21]

# Index functions on lists. Give the value to get the index of that value in the list.
print(MY_FRIENDS.index("Swaroop"))
print(MY_LUCKY_NUMBERS.index(21))

# Clear function - This empties the string.
TEMPORARY_LIST=["Headsets","Mobiles",9550328609]
print(f"Before clearing the variable the values of TEMPORARY_LIST are {TEMPORARY_LIST}")
TEMPORARY_LIST.clear()
print(f"Before clearing the variable the values of TEMPORARY_LIST are {TEMPORARY_LIST}")

# Copy Function - Copying one list to another.
MY_FRIENDS_NEW=MY_FRIENDS #There will be no new memory allocated for MY_FRIENDS_NEW. The address of MY_FRIENDS is pointed to MY_FRIENDS_NEW.
print(f"Copying MY_FRIENDS values to MY_FRIENDS_NEW without using copy function. \nThe address of MY_FRIENDS is {id(MY_FRIENDS)}\nThe address of MY_FRIENDS_NEW is {id(MY_FRIENDS_NEW)}")

MY_FRIENDS_COPY=MY_FRIENDS.copy()
print(f"Copying MY_FRIENDS values to MY_FRIENDS_COPY using copy function. \nThe address of MY_FRIENDS is {id(MY_FRIENDS)}\nThe address of MY_FRIENDS_COPY is {id(MY_FRIENDS_COPY)}")

# Appending lists - Adding new data to the end of the string
MY_FRIENDS.append("Mohan")
print(f"My New Friends after appending a new friend is {MY_FRIENDS}")

# Inserting into lists at indexes.
MY_LUCKY_NUMBERS.insert(0,1) # 0 is the index and 1 is the value at that index.
print(f'Updated MY_LUCKY_NUMBERS list is {MY_LUCKY_NUMBERS}')
MY_LUCKY_NUMBERS_IN_THIRTIES=[30,33,39]
MY_LUCKY_NUMBERS_IN_THIRTIES.insert(0,MY_LUCKY_NUMBERS) #This adds the list MY_LUCKY_NUMBERS as another List in MY_LUCKY_NUMBERS_IN_THIRTIES
print(f"Updated MY_LUCKY_NUMBERS including the thirties {MY_LUCKY_NUMBERS_IN_THIRTIES}")

# Extend Function - Adds new list variable as data not as another list type.

MY_LUCKY_NUMBERS_IN_SIXTIES=[60,66]
MY_LUCKY_NUMBERS_IN_SIXTIES.extend(MY_LUCKY_NUMBERS) # This adds the values of MY_LUCKY_NUMBERS in MY_LUCKY_NUMBERS_IN_SIXTIES not in last format.
print(f"MY_LUCKY_NUMBERS_IN_SIXTIES extend with MY_LUCKY_NUMBERS is {MY_LUCKY_NUMBERS_IN_SIXTIES}")

#Remove a value from the Lists
MY_LUCKY_NUMBERS.remove(1)
print(f"Removing the value \'1\' as one of MY_LUCKY_NUMBERS. Updated MY_LUCKY_NUMBERS {MY_LUCKY_NUMBERS}")
MY_LUCKY_NUMBERS_IN_SIXTIES.pop() # Removes the last value in the list MY_LUCKY_NUMBERS_IN_SIXTIES
print(f"After using pop() function which removes the last value in the list {MY_LUCKY_NUMBERS_IN_SIXTIES}")
MY_LUCKY_NUMBERS_IN_SIXTIES.pop(2) # Removes the values in the indexes 2.
print(f"After using pop(2) on MY_LUCKY_NUMBERS_IN_SIXTIES is {MY_LUCKY_NUMBERS_IN_SIXTIES}")

# Reversing a list.
MY_FRIENDS.reverse()
print(f"MY_FRIENDS after reversing is {MY_FRIENDS}")

# Soring a list
MY_LUCKY_NUMBERS_IN_SIXTIES.sort()
print(f"Sorting MY_LUCKY_NUMBERS_IN_SIXTIES in ascending order {MY_LUCKY_NUMBERS_IN_SIXTIES}")
MY_LUCKY_NUMBERS.sort(reverse=True) # Use this for descending order
print(f"Sorting MY_LUCKY_NUMBERS in desending order {MY_LUCKY_NUMBERS}")

'''
MY_LUCKY_NUMBERS.sort()
MY_LUCKY_NUMBERS.reverse()
Use the above statements at a time to get the desending order.
'''

