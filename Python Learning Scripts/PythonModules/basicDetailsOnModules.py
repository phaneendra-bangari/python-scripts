#Importing your own modules
#Create a python file - with .py extention and import it using the command import pythonfilename
import defaultvalues #Here defaultvalues is a .py file at the same location and I am reusing the functionalities of this external file in this file.
print(f"Values of myfavnumbers from defaultvalues.py using import command is {defaultvalues.myfavnumbers}") #myfavnumbers is a variable in defaultvalues.py file in the same folder.

#Use this command to get all the default modules in Python3
help("modules")

#Use the below command to get more help on any specific module.
#print(dir("math"))

#To get more details on each attribute of a module, use the below command
#help("math")

#Please use these commands on command line rather than on scripts as this is just for understanding.

#We even have third party modules which are supported by Python. These needs to be externally imported using "pip"

#Another way of importing modules is using from. Using this, we no need to give the module name again and again while calling the variables in that module. Follow the below example.
from math import *
print(f"The value of PI using the from import type is {pi}")

#More examples in using Modules
from math import pi,pow #Only two variables/functions will be imported and you can use them.
import math as m #You can use "m" to access all the variables or functions in math if you do a import this way. 
import platform,os,sys,math,subprocess # You can import multiple modules this way.
