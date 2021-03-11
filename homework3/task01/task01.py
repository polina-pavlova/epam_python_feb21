from typing import Callable


def cache(times=0):
    counter = 0

    def cached(func: Callable) -> Callable:
        cached_results = {}

        def func_cache(*args):
            if args in cached_results:
                nonlocal counter
                while counter < times:
                    counter += 1
                    return cached_results[args]
            cached_results[args] = func(*args)
            return cached_results[args]

        return func_cache

    return cached
