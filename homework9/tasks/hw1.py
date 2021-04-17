"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from bisect import insort
from pathlib import Path
from typing import Iterator, List, Union


def values_from_file_generator(file):
    with open(file, "r") as fi:
        yield from (int(line) for line in fi)


def get_next_value(file, files):
    try:
        return next(file)
    except StopIteration:
        files.remove(file)


def merge_sorted_files(file_list) -> Iterator:
    files_values = [values_from_file_generator(file) for file in file_list[1:]]
    current_result = [*values_from_file_generator(file_list[0])]
    while files_values:
        for file in files_values:
            value = get_next_value(file, files_values)
            if value is not None:
                insort(current_result, value)
    yield from current_result
