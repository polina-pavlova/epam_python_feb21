import pytest

from homework9.tasks.hw1 import merge_sorted_files


def test_merge_sorted_files():
    test_files = [
        "./tests/f1.txt",
        "./tests/f2.txt",
        "./tests/f3.txt",
        "./tests/f4.txt",
        "./tests/f5.txt",
    ]
    assert list(merge_sorted_files(test_files)) == [
        -1,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ]
