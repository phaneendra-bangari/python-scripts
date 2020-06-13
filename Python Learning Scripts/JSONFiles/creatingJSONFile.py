#JSON File creation using Python.
import json
FILE_CREATION='/home/ec2-user/Scripts/python-scripts/Python Learning Scripts/JSONFiles/sampleJSON_File_Created_by_Script.json'

FILE_CREATED_OBJ=open(FILE_CREATION,'w')
DIC_DATA={'Name':'Phaneendra','Skills':['GIT','Python','Shell Scripting'],'Experience':'5 Years'}
json.dump(DIC_DATA,FILE_CREATED_OBJ,indent=4)
FILE_CREATED_OBJ.close()

