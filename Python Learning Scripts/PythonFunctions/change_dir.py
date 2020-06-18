#This program is to change the directory and handling the exceptions when any errors occur.
import os
def main():
    print(f"The current working directory is: {os.getcwd()}") 
    INPUT_DIR=input("Enter the path where you want to navigate: ")
    try:
        os.chdir(INPUT_DIR)
        print(f"The current directory is changed to {os.getcwd()}")
    except FileNotFoundError:
        print("The given path is not a valid path. Please give a valid directory.")
    except NotADirectoryError:
        print("The given path is not a directory. Please give a valid directory.")
    except PermissionError:
        print("You dont have access navigate to this directory.")
    except Exception as e:
        print(e)
    return None

if __name__ == '__main__':
    main()

