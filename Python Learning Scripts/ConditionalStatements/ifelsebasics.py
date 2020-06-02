#Simple If Statement
READ_NUMBER1=eval(input("Enter a number to do comparision: "))
READ_NUMBER2=eval(input("Enter another number to do comparision: "))

if READ_NUMBER1>READ_NUMBER2:
    print(f"{READ_NUMBER1} is greater than {READ_NUMBER2}")
elif READ_NUMBER2>READ_NUMBER1:
    print(f"{READ_NUMBER2} is greater than {READ_NUMBER1}")
else:
    print(f"Both the numbers entered are equal.")

MY_LUCKY_NUMBERS=[3,9,12,21,30,33,48]
READ_LUCKY_NUMBER=eval(input("Enter any number between 0 - 50 to checkif it is your lucky number or not: "))

if READ_LUCKY_NUMBER in MY_LUCKY_NUMBERS:
    print(f"{READ_LUCKY_NUMBER} is one of your lucky numbers.")
else: 
    print(f"{READ_LUCKY_NUMBER} is not your lucky numbers")


READ_NUMBER_CHECK=eval(input("Enter a number in between 1-10 to convert into word format: "))

MY_NUMBERS={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"}

if READ_NUMBER_CHECK in [1,2,3,4,5,6,7,8,9,10]:
    print(f"Converting {READ_NUMBER_CHECK} to word results to: {MY_NUMBERS.get(READ_NUMBER_CHECK)}")
else:
    print("Please enter the numbers range from 1-10 only")

