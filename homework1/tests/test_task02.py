import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
            ],
            True,
        ),
        ([0, 1, 1, 3, 4], False),
        ([-1, -1, -2, -3], False),
    ],
)
def test_check_fibonacci(data, expected_result):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result
