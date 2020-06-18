#Key word based arguments.
def addition(DEF_VAL,**karg): #This is how we pass a variable with data.
    print(f"Given values are: {karg}")
    print(f"The type of the given values are {type(karg)}")
    for VALUE in karg:
        print(f"The addition of the given values {karg[VALUE]} with the default value {DEF_VAL} is {DEF_VAL+int(karg[VALUE])}")
addition(10,a=10,b=40,c=74)

