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
        nonlocal cached_results
        if args:
            if args in cached_results:
                return cached_results[args]
            cached_results[args] = func(*args)
            return cached_results[args]
        if kwargs:
            kwargs_ = tuple(sorted(kwargs.items()))
            if kwargs_ in cached_results:
                return cached_results[kwargs_]
            cached_results[kwargs_] = func(**kwargs)
            return cached_results[kwargs_]

    return func_cache
