# Usage of dir output functions on Strings.
MY_NAME="Phaneendra Bangari PYTHON"

#Basic operations on Strings.
print(f'Lower Case of {MY_NAME} is {MY_NAME.lower()}')
print(f'Upper Case of {MY_NAME} is {MY_NAME.upper()}')
print(f'Swap Case of {MY_NAME} is {MY_NAME.swapcase()}')
print(f'Capitalize of {MY_NAME} is {MY_NAME.capitalize()}')
print(f'Case Fold of {MY_NAME} is {MY_NAME.casefold()}')
print(f'Title of {MY_NAME} is {MY_NAME.title()}')
print(f'DIR function gives all the operations performed on that, here they go - {dir(MY_NAME)}')

#Basic Boolean Operations on Strings.
print(f'Is the string starting with P {MY_NAME.startswith("P")}')
print(f'Is the string ending with PYTHON {MY_NAME.endswith("PYTHON")}')
print(f'Is the string lower case letters {MY_NAME.islower()}')
print(f'Is the string upper case letters {MY_NAME.isupper()}')
print(f'Is the string a Title {MY_NAME.istitle()}')
print(f'Is the string consisting of alphabets {MY_NAME.isalpha()}')
print(f'Is the string a space character {MY_NAME.isspace()}')
print(f'Is the string containing numeric characters {MY_NAME.isnumeric()}')
