import csv
req_file_path="/home/ec2-user/Scripts/python-scripts/Python Learning Scripts/CSVFiles/employeeDetails.csv"

IMPORTED_CSV=open(req_file_path,'r')
content=csv.reader(IMPORTED_CSV,delimiter=",")
'''
for each in content:
    print(each) # One way to get the data of the csv file.
'''
#LIST_CONTENT=list(content) # To pring the data in list format.
#print(f"The header is as below: \n {LIST_CONTENT[0]}") # To access the first row of the csv file.
header=next(content) #This is used to move to the next row of the content data. and stores the first row into header.
print("The header is as below: \n", header)
#print(f"The length of the rows with data is: {len(LIST_CONTENT)}")
IMPORTED_CSV.close()
