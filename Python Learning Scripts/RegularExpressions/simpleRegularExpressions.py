import re
SOME_RANDOM_TEXT="This is Python learning. Its easy to learn and implement Python for automations. Its also fun."
MY_PATTERN="i[ston]"
MY_PATTERN1='Python'
print(re.findall(MY_PATTERN,SOME_RANDOM_TEXT))
print(re.findall(MY_PATTERN1,SOME_RANDOM_TEXT))

MY_PATTERN2="P[x-z][t-z][h-z][o-z]n" #x-z involves - x,y,z at that place. It holds the pattern starting with P and ends with n.
print(re.findall(MY_PATTERN2,SOME_RANDOM_TEXT))

MY_PATTERN_DOT='\.' #. is a special character, if you want to search for . use the \ before .
IP_PATTERN="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(MY_PATTERN_DOT,SOME_RANDOM_TEXT))

'''
\d - matches any decimal value.
\w - matches any single letter, digit and _
\W - matches anything which is not \w
. - matches any single character except new line character.

'''
IP_OF_MACHINE="222.222.222.222"
print(re.findall(IP_PATTERN,IP_OF_MACHINE))


        
