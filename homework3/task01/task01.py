from typing import Callable


def cache(times=1):
    counter = 0

    def cached(func: Callable) -> Callable:
        cached_results = {}

        # def func_cache(*args, **kwargs):
        # if (args + tuple(kwargs.items())) in cached_results:
        #     nonlocal counter
        #     while counter < times:
        #         counter += 1
        #         return cached_results[(args + tuple(kwargs.items()))]
        # cached_results[(args + tuple(kwargs.items()))] = func(*args,  **kwargs)
        # return cached_results[(args + tuple(kwargs.items()))]
        def func_cache(*args, **kwargs):
            if (args + tuple(kwargs.items())) not in cached_results:
                cached_results[(args + tuple(kwargs.items()))] = (
                    func(*args, **kwargs),
                    times,
                )
            else:
                value, counter = cached_results[(args + tuple(kwargs.items()))]
                if counter == 0:
                    return func(*args, **kwargs)
                else:
                    cached_results[(args + tuple(kwargs.items()))] = (
                        value,
                        counter - 1,
                    )
                    return value

        return func_cache

    return cached
