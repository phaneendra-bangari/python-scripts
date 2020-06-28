import re

MULTI_LINE='''This is great working with Python.
Its very easy.
This is fun working with Python'''

SEARCH_STRING='working'
print(re.search(SEARCH_STRING,MULTI_LINE)) #This returns an object of the first pattern match in the MULTI_LINE

SEARCH_OBJECT=re.search(SEARCH_STRING,MULTI_LINE,re.I)
print("Search found as: ", SEARCH_OBJECT.group())
print("Search index starts at: ", SEARCH_OBJECT.start())
print("Search index ends at: ", SEARCH_OBJECT.end()-1)
print("Lenth of the searched value: ", SEARCH_OBJECT.end()-SEARCH_OBJECT.start())

MATCH_STRING='THIS'
#match uses to find only at the 0th index position of a string.
MATCH_OBJ=re.match(MATCH_STRING,MULTI_LINE,re.I) #THIS wont be searched in other lines even if you explicitly ask for.
print(MATCH_OBJ)
