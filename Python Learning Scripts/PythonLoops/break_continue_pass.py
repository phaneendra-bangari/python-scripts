#Understanding Break Pass and Continue

for each in [2,4,5,6,633,212]:
    print(each)
    if each > 10:
        break #This make sures to exit out of the loop once the each value is greater than 10
print("---------------------------")
for each2 in range(0,10):
    if each2 > 3: #Till this condition is true, the print statement wont execute.             
        continue
    print(each2)

