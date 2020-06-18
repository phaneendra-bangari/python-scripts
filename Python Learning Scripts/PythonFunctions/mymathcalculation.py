#This script performs the basic airthemetic operations.

def addition(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
    return None

def subtraction(a,b):
    print(f"Subtraction of {a} and {b} is {a-b}")
    return None

def multiplication(a,b):
    print(f"Multiplication of {a} and {b} is {a*b}")
    return None

def main():
    a=10
    b=30
    addition(a,b)
    subtraction(a,b)
    multiplication(a,b)
    addition(40,80)
    subtraction(90,20)
    multiplication(80,20)
    return None

if __name__ == "__main__": #The main function executes only when the script is executed. It wont execute when we import this script from other script.
    main()
#__name__ is a vaiable which carries __main__ when the script is executed and __scriptname__ when this script is used by other script.
