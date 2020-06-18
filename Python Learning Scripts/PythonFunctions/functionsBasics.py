#to understand functions.

def welcome():
    print("Hello! Welcome All.")
    print("I am writing this from welcome user defined functions.")
    return None #Best practice.

def welcome_person(INPUT_NAME):
    print(f"Hey! {INPUT_NAME} how are you? Hope so you are doing good.")
    return None #Best practice.
#First you should define the function before calling it. Above is the defination of the function. Below is the calling of the function.
welcome()
INPUT_NAME=input("Enter your name: ")
welcome_person(INPUT_NAME)

