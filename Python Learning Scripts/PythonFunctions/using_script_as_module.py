#Using another script as module.
import mymathcalculation #Using this we can use the functions and variables declared in mymathcalculation.py script.
def main():
    mymathcalculation.addition(90,40)
    mymathcalculation.subtraction(40,10)
    mymathcalculation.multiplication(30,21)

if __name__ == "__main__":
    main()

