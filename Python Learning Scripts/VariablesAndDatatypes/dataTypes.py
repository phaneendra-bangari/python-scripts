#!/usr/bin/python3
#Owner: Phaneendra Bangari
#Contact: 09550328609
#Email: phaneendra.bangari@gmail.com

'''
I am learning and writing Python Scripting to make Automation.
Purposedly I am using GITLAB to maintain the versions of files.
'''

#This Python Script is to understand Datatypes, Datatype conversions and more.

#Variable Declaration
VARIABLE_1=20
#Printing the variables and strings in a single print statement.
print(f"Address location of VARIABLE_1 is {id(VARIABLE_1)}.\nValue of VARIABLE_1 is {VARIABLE_1}")

#Use the below print function for 2.X versions of Python.
#print("Address location of VARIABLE_1 is {} .\nValue of VARIABLE_1 is {}".format(id(VARIABLE_1),VARIABLE_1))

#Types of Variables
VARIABLE_INTEGER=30
VARIABLE_FLOAT=30.5
VARIABLE_BOOL=False
VARIABLE_STRING="Python Scripting"

#Printing the Type of the Variables
print(f"The type of the variable VARIABLE_INTEGER is {type(VARIABLE_INTEGER)} and its value is {VARIABLE_INTEGER}")
print(f"The type of the variable VARIABLE_FLOAT is {type(VARIABLE_FLOAT)} and its value is {VARIABLE_FLOAT}")
print(f"The type of the variable VARIABLE_BOOL is {type(VARIABLE_BOOL)} and its value is {VARIABLE_BOOL}")
print(f"The type of the variable VARIABLE_STRING is {type(VARIABLE_STRING)} and its value is {VARIABLE_STRING}")

#Type Conversions & Input/Output checks. We cannot convert a string to other datatypes.
VARIABLE_INPUT_STRING=input("Enter your name: ") 
#By default, it takes the data type as string

VARIABLE_NUMBER=eval(input("Enter any number to perform square of it: ")) 
#Eval function converts the string to its respective input type.

VARIABLE_RESULT=VARIABLE_NUMBER*VARIABLE_NUMBER
VARIABLE_RESULT_INTEGER=int(VARIABLE_RESULT)
#Type conversion to Integer value, whatever the type the above operation results in it.

print(f"Hello {VARIABLE_INPUT_STRING}")
print(f"The square of {VARIABLE_NUMBER} is {VARIABLE_RESULT} and result after type conversion to integer is {VARIABLE_RESULT_INTEGER}.")
	 
