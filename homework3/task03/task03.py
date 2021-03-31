# I decided to write a code that generates data filtering object from a list of keyword parameters:
from inspect import isfunction
from typing import Any, Callable


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria

    #>>> Filter.apply(1, 2, 3.0, lambda x: x + 1, lambda x: x % 2 == 0)
    [2, 3, 4.0]

    # >>> positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)])
    # >>> positive_even.func(range(10))
    # [2, 4, 6, 8]
    """

    def __init__(self, *functions: Callable[[Any], Any]):
        self.functions = functions

    def apply(self, data: Any):
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []

    def keyword_filter_func(item_of_data: dict):
        for key, value in keywords.items():
            if item_of_data.get(key) != value:
                return False
        return True

    filter_funcs.append(keyword_filter_func)

    return Filter(*filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

# print(make_filter(name='polly', type='bird').apply(sample_data))
