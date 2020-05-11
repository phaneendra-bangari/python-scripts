'''
Tuples - An empty tuples boolean value is False.
You can add a list in a tuples.
Tuples are immutable, we cannot change a part of the tuple data. Its same like strings.
Hence, Lenght, count and index are only available for Tuple.
Use tuple for the data which needs not to be changed.
'''

MY_FAMILY="Father","Mother","Brother","Sister" # This is also a tuple declaration.
print(f"The content of MY_FAMILY are {MY_FAMILY} and the type is {type(MY_FAMILY)}")

EVEN_NUMBERS=(2,4,6,8,10) # This is another type of tuple declaration.
print(f"The content of EVEN_NUMBERS are {EVEN_NUMBERS} and the type is {type(EVEN_NUMBERS)}")

STOCK_VALUES=(1,2,3,[4,4.5,4.7,4.9],4,9,10) # We can even add a list in a tuple.
print(f"The content of STOCK_VALUES are {STOCK_VALUES} and the type is {type(STOCK_VALUES)}")
print(f"Accessing the list part of the tuple STOCK_VALUES i.e Second element of the list in the tuple. \n{STOCK_VALUES[3][1]}")

# Length operation on tuples
print(f"Length of the STOCK_VALUES is {len(STOCK_VALUES)}")

# Count operation on Tuples
print(f"Count of the value \'4\' in STOCK_VALUES is {STOCK_VALUES.count(4)}") #The value inside the list is not counted as value 4.

# Index operation on tuples
print(f"Index of the value \'10\' in STOCK_VALUES is {STOCK_VALUES.index(10)}")

