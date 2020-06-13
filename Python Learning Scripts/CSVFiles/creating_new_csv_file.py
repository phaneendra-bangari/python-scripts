#To create a new CSV file using Python.
import csv
FILE_TO_CREATE="/home/ec2-user/Scripts/python-scripts/Python Learning Scripts/CSVFiles/generatedusingPythonScript.csv"

CSV_FILE_OBJ=open(FILE_TO_CREATE,'w',newline="")
CSV_WRITER=csv.writer(CSV_FILE_OBJ,delimiter=",")

DATA_LIST=[['Name','Age'],['Phaneendra','26'],['Mohan','30'],['Teja','27']]
CSV_WRITER.writerows(DATA_LIST)
CSV_WRITER.writerow(['Kiran','26'])
CSV_FILE_OBJ.close()
