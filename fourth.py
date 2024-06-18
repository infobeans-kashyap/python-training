# Basics of Python part-4 (lists, dictionaries, tuples & sets)

list_a = [1,3,5]

print('*'*10,'List & list functions','*'*10)
print(list_a[1])

print('Demo of converting a string to list', list('Hello World'))

print('To find if a character is within a list  : ', 3 in list_a )

print('To find if a character is not within a list : ', 3 not in list_a )

list_a.append(6)
print('To append items to a list', list_a)

list_a.insert(0,7)
print('To insert items to a specific index in a list', list_a)

list_a.remove(7)
print('To remove items from a list', list_a)

list_a.clear()
print('To remove all items from a list', list_a)

list_a = [1,3,1,2,3,5]
list_a.pop()
print('To remove the last item using pop()', list_a)

print('To get the index of the item based on value', list_a.index(3))

print('To count the occurrence of a given value in a list', list_a.count(3))

list_a.sort()
print('To sort the values within the list in ascending order', list_a)

list_a.sort(reverse=True)
print('To sort the values within the list in descending order', list_a)

list_a.reverse()
print('To reverse the values within the list ', list_a)

list_b = list_a.copy()
list_a[2] = 4
print('To copy one list to another ', list_b)

print('To return the max value form the list ', max(list_b))

print('To return the min value form the list ', min(list_b))

del list_a[0]
print('Usig del statement to delete a value from list', list_a)

list_str = ['this', 'is', 'a', 'string', 'list']
list_str.reverse()
print(list_str)

list_str.sort()
print(list_str)
print('*'*10,'Dictionaries and dictionaries functions','*'*10)

persons1 = {
	'Name' : 'Xyz',
	'Age' : '30',
    'Key' : 'value',
    'Key' : 'value'
}


print(persons1.get('Nam2'))

persons2 = {
	'Name' : 'Xyz',
	'Age' : '30',
    'Key' : 'value',
    'Key' : 'value'
}

print('In and not in methods for dictionary', 'Name' in persons1)

print('Return all the keys from a dictionary using keys() method ', persons2.keys())

print('Return all the values from a dictionary using values() method ', persons2.values())

print('Return all the key and values pair from a dictionary using values() method ', persons2.items())

print('Printing out all key value pairs using items method')
for k, v in persons2.items() :
    print(('Key is {} => value is {}').format(k, v))

print('Check if a value exists in a dictionary', 'Xyz' in persons2.values())

print('Check if a key exists in a dictionary using the get() method : ', persons2.get('Name','The key providied not exists'))

print('Creating a new dict using fromkeys() method with none values', {}.fromkeys(['key1','key2']))

print('Creating a new dictionary using fromkeys() method', {}.fromkeys('ab','value'))

persons2.pop('Key')
print('Using pop() method on a dictionary : ', persons2)

persons1.popitem()
print('Using popitem() on a dictionary',persons1)

dict_1 = {'city':'Pune', 'temperature':40, 'humidity': 50}
dict_2 = {'population': 2340000, 'GDP' : 3200}

dict_1.update(dict_2)
print('Using the update() method on a dictionary ', dict_1)

print('*'*10, 'Tuples', '*'*10)

tup_a = (1, 4, 6, 8, 20, 13, 1, 6)
print('Tuple : ', tup_a)

tup_b = tuple([1, 3, 5, 9, False, True])
print('Using the "tuple" function with list as argument : ', tup_b)

tup_c = tuple('hello!!3')
print('Using the "tuple" function with string as argument : ', tup_c)

print('Accessing tuple items via index : ', tup_c[3])

print('Accessing tuple items via slice : ', tup_c[2:5])

print('Accessing tuple items via slice with step : ', tup_c[2::5])

print('Using count method to find number of times a value occurrs in a tuple : ', tup_a.count(1))

print('Using index method to find the key of based on a value in a tuple : ', tup_a.index(1))

set_a = {1,4,5,6}

print('Sets created using curly brackets "{}"',set_a)
set_b = set({'a','b','c'})

print('Sets created using "set" fucntion',set_b)

set_c = {1, 2, 3, 5, 1, 6, 7, 1}

print('Duplicate items will be ignored in a set',set_c)

set_d = set(range(1,6))
print('Set created using range as argument to set function : ', set_d)

set_e = {even+2 for even in range(2,11,2)}

print('Creating a set using set comprehensions ', set_e)