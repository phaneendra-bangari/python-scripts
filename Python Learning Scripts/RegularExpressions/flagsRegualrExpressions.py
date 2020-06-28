import re
MULTI_LINE='''This is Python in line one.
This is Python in line two
THIS IS PYTHON IN LINE TWO
THis is PYTHON in LINE TWo'''

PATTERN_FLAG=r"This"
print(re.findall(PATTERN_FLAG,MULTI_LINE,re.I|re.M)) #re.I for IGNORECASE. re.M for Multiline search.
PATTERN_FLAG_1=r'Two$'
print(re.findall(PATTERN_FLAG_1,MULTI_LINE,re.I))
