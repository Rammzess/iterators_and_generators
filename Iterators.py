import matplotlib

nest_list = [
	['dsf', 'tyuty', 'zxczv', True, 383],
	['n,nm', 'wew', 'rr', 'qqq', False],
	[444, [1, 2], None],
]

# Вариант 1
# итератор
final_list = []
class NestListIterator:

    def __init__(self, start, end, nest_list):
        self.nest_list = nest_list
        self.start = start
        self.end = end

    def __iter__(self):
        self.start = -1
        return self
    
    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.nest_list[self.start]

# генератор
def list_of_lists(nest_list):
    for list_item in nest_list:
        for item in list_item:
            yield item

# Вариант 2 принимает любую вложенность,
# с вызовом функции внутри себя
def lists_list(nest_list):
    result = list()
    for element in nest_list:
        if isinstance(element,list):
            result.extend(lists_list(element))
        else:
            result.append(element)
    return result


# Вызов
if __name__ == '__main__':
    #итератор - в список
    for item in NestListIterator(1, len(nest_list), nest_list):
        for item_1 in NestListIterator(1, len(item), item):
            final_list.append(item_1)
        print(final_list)

    #генератор - в список
    flat_list = [item for item in list_of_lists(nest_list)]
    print(flat_list)
    
    #функция с вызовом внутри себя и разбирает любую вложенность
    print(lists_list(nest_list)) 
    
    # Вариант 3 с помощью библиотеки, любая вложенность
    print(list(matplotlib.cbook.flatten(nest_list)))