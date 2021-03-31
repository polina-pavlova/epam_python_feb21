import pytest

from homework4.tasks.task_5_optional import fizzbuzz


def test_15_numbers():
    assert list(fizzbuzz(15)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
    ]


def test_zero():
    assert list(fizzbuzz(0)) == []
