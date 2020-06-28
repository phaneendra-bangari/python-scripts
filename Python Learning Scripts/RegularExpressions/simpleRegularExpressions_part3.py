import re

SOME_TEXT="aaabbbccc abc abbbbbbbbbbbbbbbbbbbbbbbc ac"
PATTERN_1="a{3}b{3}c{3}" # Its a pattern which searchs for a three times b three times and c three times.
print(re.findall(PATTERN_1,SOME_TEXT))

PATTERN_2=r"a{1,3}b{1,3}c{1,3}" #1, 2, 3 times repeat.
print(re.findall(PATTERN_2,SOME_TEXT))

PATTERN_3=r"\ba{1,}b{2,}c{1,}\b" #b repeats more than 2 times. 
print(re.findall(PATTERN_3,SOME_TEXT))

'''
+ is for one or more. Replaces with {1,}
* is for O or more. 
? once or none
'''
