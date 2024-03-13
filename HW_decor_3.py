import os
from HW_decor_2 import logger
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = change_list(list_of_list)

    def __iter__(self):
        self.items = iter(self.list_of_lists)
        return self

    def __next__(self):
        item = next(self.items)
        return item

    if os.path.exists('log_4.log'):
        os.remove('log_4.log')

@logger('log_4.log')
def change_list(new_list):
    temp = new_list
    result = []
    check = True
    while check:
        result = []
        check = False
        for i in temp:
            if isinstance(i, list):
                check = True
                result.extend(i)
            else:
                result.append(i)
        temp = result
    return result


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()