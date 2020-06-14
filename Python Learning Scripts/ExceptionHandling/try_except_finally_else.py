# Usage of Try and Expect.
try:
    print(4/2)
except ZeroDivisionError:
    print("Zero Division Error Exception error.")
except Exception as e:
    print(e)
else:
    print("This will execute only if there are no exceptions in the try block.")
finally:
    print("This will execute anyway.")


