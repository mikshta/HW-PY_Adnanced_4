print('ЗАДАНИЕ 1')
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class SampleIterator():
    def __init__(self, data):
        self.data = data
        
    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        list_of_el = []
        for element in self.data:
            for item in element:
                list_of_el.append(item)
        if self.cursor == len(list_of_el)-1:
            raise StopIteration  # выход из цикла
        self.cursor += 1
        return list_of_el[self.cursor]
        # в цикле for item in SampleIterator() returned_item подставится в item


test = SampleIterator(nested_list)
for element in test:
    print(element) # при каждой итерации выполняется __next__ и результат подставляется в item. 
        # Когда выбрасывается StopIteration цикл завершается
        
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