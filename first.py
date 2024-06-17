# Basics of Python part-1

ex_var = 5;
print(ex_var);
ex_var = 7;
print('Total' , 11%3 + ex_var, 'MMM');
ex_float = 1.23
print('-'*10,'Math operations','-'*10);
print('Approximation errors in float demo :', 1.23+2.80);
print('Mehod -1 : Solving approximation error in floats : ',(123+280)/100);
print('Mehod -1 : Solving approximation error in floats : ',round(1.23+2.80,2));

# A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:

print('Penne 16 oz Pack of 12 - $',16.68);

print('Arrabiata Pasta Sauce 24 oz - $',6.98);

print('Bag of 20 Organic Garlic Cloves - $',16.78);

print('Italian Seasoning 1.5 oz Bottle - $',15.26);

print('Artisan Baguettes Twin Pack - $',3.00);

print('12 oz Bag of Meatballs - $',4.39);

print('The customer has to pay a total of (with approximation error): ', (16.68+6.98+16.78+15.26+3+4.39));
print('The customer has to pay a total of (without approximation error, by converting to integers): ', (1668+698+1678+1526+300+439)/100);
print('The customer has to pay a total of (without approximation error by using round): ', round((16.68+6.98+16.78+15.26+3+4.39),2));

print('-'*10,'String operations','-'*10);

ex_fnm = 'kashyap'
print('Original String : ',ex_fnm)
print('Accessing the first character of the string : ',ex_fnm[0])
print('Accessing the characters based on index directly on string : ', 'kashyap'[0])
print('Slicing a string from start to 3 places ',ex_fnm[:3])
print('Slicing a string from 2 and going to 3 places (2+3) ',ex_fnm[2:5])
print('Slicing a string from 2 till end ',ex_fnm[2:])

ex_lnm = 'padh'
ex_full_name = ex_fnm + ex_lnm
print('Simple concatenation: ', ex_full_name)

print('-'*10,'Few Common functions','-'*10)
print('Type function for string var', type(ex_fnm), 'Type function for int var',type(ex_var), 'Type funciton for float var', type(ex_float))
print('Convert any variable(int,float,boolean) to string using str() function ',type(str(ex_var)))
print('-'*10,'Few Escape characters','-'*10)
print('This\tis\ta\tdemo\tof', ("'/\\t/'"))
print('This\nis a demo of', ("'/\\n/'"))
print('This is a demo of "\\\"')
print('This is a demo of backslash \\')
text = "This is a test"
print(text, "\b\bHere")  # Try to backspace twice and print "Here"
print('This is an example of \a character')
# \a: Inserts an alert (beep) character.

print('This is an example of /\f/\f character')
# \f: Inserts a form feed character.
print('This is an example of \v character')
# \v: Inserts a vertical tab character.
print('Printing an asetrics triangle\n')
print('*'*7,'\n',
      '*'*5,'\n',
      '*'*3,'\n',
      '*')
print('*'*10,'Input function','*'*10)
input_var = input('Enter your name : ')
print('Yout entered ', input_var)

print('*'*10,'Using int() & float() functions', '*'*10)
ex_input = input('Enter a number :');
print('The input is of type ', type(ex_input))
print('Using int() function, we converted to type ', type(int(ex_input)))
print('Using float() function, we converted to type ', type(float(ex_input)))
print('Using int() funciton on float value', int(11.9))