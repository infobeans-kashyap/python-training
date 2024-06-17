# Basics of Python part-2 (functions, flow controls, range, len, for loop, while loop)

# def function1():
#     ex_input = input('Enter any value : ')
#     return ex_input


# print('Simple function call with output : ',function1())

# def function2(a,b):
#     a = int(a)
#     b = int(b)
#     return a*b

# ex_1 = input('Enter first number : ')
# ex_2 = input('Enter second number : ')
# print('Call to function with parameters : ', function2(ex_1,ex_2))

# def function3(a,b=2):
#     a = int(a)
#     b = int(b)
#     return a*b

# ex_1 = input('Enter first number : ')
# # ex_2 = input('Enter second number : ')
# print('Call to function with default parameters : ', function3(ex_1))

print('*'*10,'Importing Modules','*'*10)
import random
print('Random integer generation using random module (Generic import): ', random.randint(1,9))

from random import randint
print('Random integer generation using random module (Function import): ', randint(1,9))

from random import *
print('Random integer generation using random module (Universal import): ', randint(1,9))


global_var = 'This is a global variable'

def print_global():
    print('Global variable accessed within a function ', global_var)

print_global()

global_var = 'This is a global variable'

def print_global():
    global global_var
    global_var = 'New value changed from function'
    print('Global variable accessed within a function with changed value', global_var)

print_global()

if(global_var):
    print('dfd')

if 'red' == global_var:
    print('red')
elif 'blac' == global_var:
    print('black')
else:
    print('not a color')

print('*'*10,'Example of Truthy & Falsy','*'*10)
age = 21
driving_test = True

if age <= 21 and driving_test:
    print('Normal operation output : Eligible to drive')
else:
    print('Normal operation output : Not eligible to drive')

age = 'any random number'
driving_test = 'any random value'

if age and driving_test:
    print('Truthy operation output : Eligible to drive')
else:
    print('Falsy operation output : Not eligible to drive')

print('*'*5,'While loop','*'*5)
a=0
while a<5:
    print('The value of a is : ',a)
    a+=1
    if(a>5):
        print('Getting out of while loop')
        break
# b = int(input('Enter any number : '))
# input = b
# total = 0
# while b > 0:
#     total += b
#     print('total : ', total)
#     b -= 1
# else:
#     print('Print else block on while loop')
# print('The number entered is : ',input)
# print('The total is : ',total)

print('\nFor each demo\n')
for i in 'hello world':
    print('The value of i is : ',i)

print('\n---Range functoin---\n')

for i in range(4):
    print('Example of range functoin ',i)
print('---\n')
for i in range(1,50) :
    if i%3==0 and i%5==0:
        print('\nFrizbuzz')
    else:
        print('Example of range functoin ',i)
print('---\n')
in_var = int(input('Enter a number : '))
factorial = 1
for i in range(factorial,in_var+1) : 
    factorial *= i
print('Factorial of ',in_var, 'is :',factorial)

for i in range(0,4,2):
    print('Example of range functoin ',i)

print('\n')
print('*'*10,'String functions','*'*10)

print('The length of <abcd> is :', len('abcd'))