"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""

from typing import List


def check_fibonacci(data: List[int]) -> bool:
    if len(data) < 3 or any(map(lambda number: number < 0, data)):
        return False
    for i in range(2, len(data)):
        if not data[i] == data[i - 1] + data[i - 2]:
            return False
    return True
