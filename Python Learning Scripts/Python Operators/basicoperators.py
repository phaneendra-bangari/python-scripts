#Airthemetic and Assingment Operators
#In Python3, a float value is returened for a divison operation.

#Asking inputs from the user
value1=eval(input("Enter the value of a"))
value2=eval(input("Enter the value of b"))

#Modulo
print(f"The value of a%b which is the reminder is {value1%value2}")

#Exponential
print(f"The value of a**b which is the exponential is {value1**value2}")

#Float Division - This gives the lowest quotient value.
print(f"The value of the quotient which is round off with the less value is {value1//value2}")

#Assingment Operators
value1 += value2
print(f"Usage of += on a and b i.e a+=b which implies a=a+b is {value1}")

#Conditional Operators
print(f"Use the operators to compare the values or strings using >,<,>=,<=,!=,==")
print(f"The ascii value of a is {ord('a')}")
print(f"The character of the ascii value 67 is {chr(67)}")

#Identity Operators - To check the type of the variables we can use this operator.
#"is" and "is not" are the two operators.

print(f"Comparing the value1 and value2 data types using is operator")
print(f"Are the data types of value1 and value2 are same: {type(value1) is type(value2)}")


#Membership Operators are "in" and "not in"
valid_java_versions=['1.2','1.5','1.8','1.9']
current_java_versions="1.5"
if current_java_versions in valid_java_versions:
    print("This is valid java version")
else:
    print("This is not a valid java version")

#Logical Operators - and, or not operators.
#Usage of All function - It is an and operator in a shorter way.
all([2>1,4>2])
#Usage of any function - It is a or operator in a shorter way.
any([4>5,6>2])

