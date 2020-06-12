'''
import subprocess
sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f'OUTPUT IS: {out}')
print(f'Error is: {err}')
==================================>
if shell=True then your cmd is a string (as your os command)
if shell=False then your cmd is a list

Note: shell=False dont work on your os environment variables

ex: cmd="ls -lrt" ==>shell=True
    shell=False ==> cmd="ls -lrt".split()  or ['ls','-lrt']
=======================================================================


shell=True always on windows
============================
cmd is a string
----------------------------------------------------------
'''

import subprocess
#Execute any command and store the ouptut in a variable.
FREE_MEMORY=subprocess.Popen('free -m',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
STATUS_OF_COMMAND=FREE_MEMORY.wait()
OUTPUT_VALUES,ERROR_VALUES=FREE_MEMORY.communicate()
print(f"The return code of the given command is: {STATUS_OF_COMMAND}")
print(f"Output of the given command is: {OUTPUT_VALUES.splitlines()}") #If you dont use splitlines() you get the output in byte format.
#print(f"Output of the given command is: {OUTPUT_VALUES}")
print(f"Error of the given command is: {ERROR_VALUES}")

INPUT_COMMAND=input("Enter any command which you want to execute.").split() #using split() you can change the string command to list type.
INPUT_COMMAND_EXECUTION=subprocess.Popen(INPUT_COMMAND,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
STATUS_OF_INPUT_COMMAND=INPUT_COMMAND_EXECUTION.wait()
OUTPUT_VALUES_INPUT,ERROR_VALUES_INPUT=INPUT_COMMAND_EXECUTION.communicate()
print(f"The return code of the execution is: {STATUS_OF_INPUT_COMMAND}")
print(f"Output of the given command is: {OUTPUT_VALUES_INPUT.splitlines()}")
print("----------------------------------------------------------------------")
print(f"Error of the given command is: {ERROR_VALUES_INPUT.splitlines()}")



