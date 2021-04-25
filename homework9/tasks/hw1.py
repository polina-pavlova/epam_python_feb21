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
from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


def values_from_file_generator(file):
    with open(file, "r") as fi:
        yield from (int(line) for line in fi)


def merge_sorted_files(file_list) -> Iterator:
    files_values = [values_from_file_generator(file) for file in file_list]
    yield from merge(*files_values)
