# I decided to write a code that generates data filtering object from a list of keyword parameters:
from inspect import isfunction


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria

    >>> Filter.func(1, 2, 3.0, lambda x: x + 1, lambda x: x % 2 == 0)
    [2, 3, 4.0]

    # >>> positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)])
    # >>> positive_even.func(range(10))
    # [2, 4, 6, 8]
    """

    #
    # def __init__(self, functions):
    #     self.functions = functions

    def func(*params):
        params: tuple = params

        functions = [param for param in params if isfunction(param)]
        args = [param for param in params if not isfunction(param)]

        def apply():
            for foo in functions:
                return [foo(arg) for arg in args]

        return apply()

    # def apply(self, data):
    #     return [item for item in data if all(i(item) for i in self.functions)]


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

    return filter_funcs
    # return Filter.func(filter_funcs)


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
# print(Filter.func(sample_data, make_filter(name="polly", type="bird")))
# print(Filter.func(sample_data, make_filter(name='polly', type='bird')))
