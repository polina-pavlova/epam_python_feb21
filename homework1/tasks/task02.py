"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""

from typing import List


def check_fib_window(a: int, b: int, c: int) -> bool:
    if all(map(lambda number: number >= 0, [a, b, c])):
        return a + b == c


def check_fibonacci(data: List[int]) -> bool:
    assert len(data) >= 3
    while len(data) >= 3:
        if not check_fib_window(data[0], data[1], data[2]):
            return False
        data = data[1:]
    return True
