import matplotlib

nest_list = [
	['dsf', 'tyuty', 'zxczv', True, 383],
	['n,nm', 'wew', 'rr', 'qqq', False],
	[444, [1, 2], None],
]

# Вариант 1
# итератор
class FlatListIterator:

    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.cursor = -0
        self.inner_cursor = -1
        return self

    def __next__(self):
        self.inner_cursor += 1

        if self.inner_cursor == len(self.main_list[self.cursor]):
            self.cursor += 1
            self.inner_cursor = 0

        if self.cursor == (len(self.main_list)):
            raise StopIteration

        return self.main_list[self.cursor][self.inner_cursor]

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
    new_flatlist = [item for item in FlatListIterator(nest_list)]
    print(new_flatlist)

    #генератор - в список
    flat_list = [item for item in list_of_lists(nest_list)]
    print(flat_list)

    #функция с вызовом внутри себя и разбирает любую вложенность
    print(lists_list(nest_list))

    # Вариант 3 с помощью библиотеки, любая вложенность
    print(list(matplotlib.cbook.flatten(nest_list)))