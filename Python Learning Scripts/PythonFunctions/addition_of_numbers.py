#Addition of two numbers.
def do_addition(a,b):
    print(f"Addition of the numbers {a} and {b} is {a+b}")
    return None

def do_subtraction(a,b):
    result=a-b
    print(f"Subtraction of the numbers {a} and {b} is {result}")
    return None

def main():
    a=eval(input("Enter the value of a: "))
    b=eval(input("Enter the value of b: "))
    do_addition(a,b) #Functions with Arguments
    do_subtraction(a,b) #Functions with Arguments
    return None

main() #First this will execute.
