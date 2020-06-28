import re

BASIC_TEXT="Python is easy to learn and it is easy to implement and teach. Python is good."
PATTERN_1="^Python" #Use this ^ to search for the pattern at the starting of the given text.
PATTERN_2="good.$" #Use this $ to search for the pattern at the end of the string.
print(re.findall(PATTERN_2,BASIC_TEXT))

BASIC_TEXT_1="Good is great. Great is Good and itsGood Good"
PATTERN_3=r"\bGood" # \b searchs for the pattern which has empty string before and after the pattern. It even includes starting and ending of the text.
print(re.findall(PATTERN_3,BASIC_TEXT_1))

PATTERN_4=r"\BGood"
print(re.findall(PATTERN_4,BASIC_TEXT_1))
'''
Similarly we have \B - Empty string not at the begining and ending of the word.
\t \n \r - Matches tab, newline, return respectively.

'''
