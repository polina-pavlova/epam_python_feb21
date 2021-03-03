import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["filename", "expected_result"],
    [("tests/task03.txt", (-4, 5))],
)
def test_find_maximum_and_minimum(filename: str, expected_result: bool):
    actual_result = find_maximum_and_minimum(filename)

    assert actual_result == expected_result
