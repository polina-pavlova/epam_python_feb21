import string

import pytest

from homework2.tasks.hw5 import custom_range


def test_custom_range_with_one_arg():
    assert custom_range(string.ascii_lowercase, end="g") == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]


def test_custom_range_with_two_args():
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_custom_range_with_three_args():
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
