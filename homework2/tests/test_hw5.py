import string

import pytest

from homework2.tasks.hw5 import custom_range


@pytest.mark.parametrize(
    ["iterable", "start", "stop", "step", "expected_result"],
    [
        (string.ascii_lowercase, "p", "g", -2, ["p", "n", "l", "j", "h"]),
        (string.ascii_lowercase, "a", "g", 1, ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            "g",
            "p",
            1,
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
    ],
)
def test_custom_range(iterable, start, stop, step, expected_result):
    actual_result = custom_range(iterable, start, stop, step)

    assert actual_result == expected_result
