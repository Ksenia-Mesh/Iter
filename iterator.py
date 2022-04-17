nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

nested_list_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

my_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', [5, 10, 'f']],
	[1, 2, None],
]

# Задача 1
class FlatIterator:
    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.multi_list_iter = iter(self.my_list)
        self.cursor = -1
        self.nested_list = []
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.nested_list) == self.cursor:
            self.nested_list = None
            self.cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.multi_list_iter)
        return self.nested_list[self.cursor]

# задача 2
def flat_generator(new_list):
    for el in new_list:
        for e in el:
            yield e

# задача 3
class FlatIterator_1:

    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.new_iter = []
        self.iter = iter(self.my_list)
        return self

    def __next__(self):
        while True:
            try:
                self.elem = next(self.iter)
            except StopIteration:
                if not self.new_iter:
                    raise StopIteration
                else:
                    self.iter = self.new_iter.pop()
                    continue
            if isinstance(self.elem, list):
                self.new_iter.append(self.iter)
                self.iter = iter(self.elem)
            else:
                return self.elem

# задача 4
def flat_generator_1(new_list):
    for el in new_list:
        if isinstance(el, list):
            for elem in flat_generator_1(el):
                yield elem
        else:
            yield el



if __name__ == '__main__':
    print('Задание 1')
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('Задание 2')
    for item in flat_generator(nested_list_1):
        print(item)
    print('Задание 3')
    for item in FlatIterator_1(my_list):
        print(item)
    print('Задание 4')
    for item in flat_generator_1(my_list):
        print(item)


