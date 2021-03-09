"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(iterable, *args):
    current = iterable[0]
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        current = args[0]
        stop = args[1]
    else:
        current = args[0]
        stop = args[1]
        step = args[2]

    result_list = []

    if iterable.index(current) < iterable.index(stop):
        while iterable.index(current) < iterable.index(stop):
            result_list.append(current)
            current = iterable[iterable.index(current) + step]

    else:
        while iterable.index(current) > iterable.index(stop):
            result_list.append(current)
            current = iterable[iterable.index(current) + step]

    return result_list
