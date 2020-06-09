#A script to clear the terminal irrespective of the Operating System.
import os
import platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

