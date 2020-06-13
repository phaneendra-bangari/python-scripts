#To access JSON File to dictionary.
import json
FILE_JSON='/home/ec2-user/Scripts/python-scripts/Python Learning Scripts/JSONFiles/sampleJSONFile.json'

JSON_OBJECT=open(FILE_JSON,"r")
#print(JSON_OBJECT.read()) # To display JSON data in string.
print(json.load(JSON_OBJECT))
JSON_OBJECT.close()

