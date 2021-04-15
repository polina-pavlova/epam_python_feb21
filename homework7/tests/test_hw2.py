import pytest

from homework7.tasks.hw2 import backspace_compare


@pytest.mark.parametrize(
    ["first", "second", "expected_result"],
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
        ("asasv#####", "", True),
    ],
)
def test_backspace_compare(first, second, expected_result):
    assert backspace_compare(first, second) == expected_result
