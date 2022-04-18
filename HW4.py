
print('ЗАДАНИЕ 1')
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in nested_list:
    printer = item.__iter__()
    for el in printer:
        print(el)

print()
print('Плоский список')
flat_list = [j for i in nested_list for j in i]

print(flat_list)
    
print()
print('ЗАДАНИЕ 2')

def flat_iterator(nested_list):
    for list_ in nested_list:
        for el in list_:
            yield el

print(*list(flat_iterator(nested_list))) 