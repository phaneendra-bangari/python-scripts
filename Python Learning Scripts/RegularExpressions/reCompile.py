import re
#creating a pattern object.
TEXT="I installed Python. Its versions are Python2 and Python3. Both are simple and easy to understand."
PATTERN=r"\bPython[23]?\b"
PATTERN_OBJ=re.compile(PATTERN,flags=re.I)
print(PATTERN_OBJ)

print(PATTERN_OBJ.findall(TEXT))

