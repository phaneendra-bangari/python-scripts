#os.system() function takes any OS command and executes and prints in the output. If the value of os.system() is assinged to a varibale it stores the return code of the operation. 0 - if the command is executed successfully and non-zero when the command is not executed successfully.

#Writing a simple script for displaying date command.

import os
print("The current date and time os the OS is: ");DATE_RETURN_CODE=os.system('date')
if DATE_RETURN_CODE == 0:
    print("Your command is successfully executed.")
else:
    print("Your command is not executed successfully.")

