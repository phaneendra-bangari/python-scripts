#Multiply two numbers using python.
def do_multiplication(a=10,b=30): #Default value should not only assigned to first value.
    return a*b

def main():
    a=eval(input("Enter the first value: "))
    b=eval(input("Enter the second value: "))
    print(f"Multiplication of the values {a} and {b} is {do_multiplication(a,b)}")
    print(f"Default addition using the same function is: {do_multiplication()}")
    print(f"Default addition using the same function is: {do_multiplication(3)}")
    print(f"Default addition using the same function is: {do_multiplication(4)}")
main()
