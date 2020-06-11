#This script takes a string as input and locates its index values using loops.

INPUT_STRING=input("Enter a string to point their index values: ")
TEMP=0
for INDEX_VALUE in INPUT_STRING:
    print(f"{INDEX_VALUE}->{TEMP}")
    TEMP=TEMP+1

'''
INPUT_STRING=list(input("Enter a string to point their index values: "))
for INDEX_VALUE in INPUT_STRING:
    print(f"{INDEX_VALUE}->{INPUT_STRING.index(INDEX_VALUE)}")
'''
