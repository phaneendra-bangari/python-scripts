#Variable length arguments.

def addition(*values): #This is the way how a function accepts multiple arguments as tuple.
    ADDED_VALUE=0
    for VALUE in values:
        ADDED_VALUE=ADDED_VALUE+VALUE
    print(f"Addition of the given numbers is {ADDED_VALUE}")
    return None
addition(3,9,10)
addition(4,3,2,41,52)
addition()
