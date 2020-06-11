# This is the usage of range() and for loop.

print(list(range(0,12,3))) #Start,Stop,Step Value

#Using for loops using Strings

STRING_1="Python Scripting"
for each in STRING_1:
    print(each)

LIST_1=["Hello",3,6]
for greet in LIST_1:
    print(greet)
print("-------------------------")
LIST_2=[(1,2),(3,5),(9,12)]
for first,second in LIST_2:
    print(first)

MY_DICT={"First Name: ":"Phaneendra","Last Name: ":"Bangari","Middle Name: ":"Kumar"}
for each_dic in MY_DICT:
    print(each_dic) #By default the Key will be printed.

for each_dic_index,each_dic_value in MY_DICT.items(): #Need to access both the Key and Value using items()
    print(each_dic_index,each_dic_value)

for each_dic_values in MY_DICT.values(): # Accessing only values
    print(each_dic_values)


