#This program is to display the inputed text aligned in Center, Left and right and in Title format.

#Importing OS Module to use the get_terminal_size function.
import os
COLUMNS_SIZE=os.get_terminal_size().columns #This returns the column size of the terminal where you are executing the script.

#Inputing a string from the user
INPUT_STRING=input("Enter any string to be displayed in 3 formats: ")

#Converting the inputed string to TITLE format using title function.
INPUT_STRING_TITLE=INPUT_STRING.title()

print(INPUT_STRING_TITLE.center(COLUMNS_SIZE)) #Pringing in Center
print(INPUT_STRING_TITLE.ljust(COLUMNS_SIZE)) #Pringing in Left Alingment
print(INPUT_STRING_TITLE.rjust(COLUMNS_SIZE)) #Pringing in Right Alingment
