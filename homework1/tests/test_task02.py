import pytest

from homework1.tasks.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (
            [0, 1, 1, 2, 3, 5],
            True,
        ),
        ([0, 1, 1, 3, 4], False),
        ([-1, -1, -2, -3], False),
        ([1, 1], False),
    ],
)
def test_check_fibonacci(data, expected_result):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result
