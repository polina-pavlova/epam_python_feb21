"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def func_cache(*args, **kwargs):
        if (args + tuple(kwargs.items())) in cached_results:
            return cached_results[(args + tuple(kwargs.items()))]
        cached_results[(args + tuple(kwargs.items()))] = func(*args, **kwargs)
        return cached_results[(args + tuple(kwargs.items()))]

    return func_cache
