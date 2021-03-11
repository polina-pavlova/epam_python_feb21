import pytest

from homework1.tasks.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum():
    assert find_maximum_and_minimum("tests/task03.txt") == (-4, 5)
