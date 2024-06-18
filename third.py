# Basics of Python part-3 (string functions)

print('*'*10,'String methods','*'*10)

str = 'This is a demo'
print('The length of the string is:', len(str))
upper =str.upper()
print('Converting the string to upper case :', upper)
print('Converting the string to all lower ', upper.lower())

print('Checking whether the string is all lower cases', upper.islower())
print('Checking whether the string is all lower cases', upper.isupper())

print('-------Some more string functions------')
print('To check if the string has only letters ', upper.isalpha())

alpha_numeric = 'Test123'
print('To check if the string has only letters & numbers ', alpha_numeric.isalnum())
numeric = '123'
print('To check if the string has only numbers ', numeric.isdecimal())
spaces_str = '   '
print('To check if the string has only numbers ', spaces_str.isspace())
title_cases = 'Test123 Da'
print('To check if the string has only title cases ', title_cases.istitle())

print('To check if the string starts with a character/string ', title_cases.startswith('Te'))
print('To check if the string ends with a character/string ', title_cases.endswith('Da'))

print('To join multiple strings ', ' '.join([alpha_numeric,numeric,title_cases]))

print('To divide a string into multiple strings ', title_cases.split(' '))

str = 'asdf   123'
print('Right justified string ',str.rjust(15))
print('Left justified string ',str.ljust(15))

print('Right justified string with other characters ',str.rjust(15,'='))
print('Left justified string with other characters ',str.ljust(15,'='))

print('Center justified string with other characters ',str.center(15,'='))

print('Remove white spaces from string ',str.strip())

print('Remove characters from string ',str.strip('3'))

str = 'abc, def, xyz, hijk'

print('Removing characters from string using strip ', str.strip(', hi jk'))

print('Replacing a string using replace method ', str.replace('a','$'))

print(('Using the format funciton to format a string with variables str {}, alpha_numeric {},title_cases {} ').format(str,alpha_numeric,title_cases) )