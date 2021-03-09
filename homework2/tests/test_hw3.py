import pytest

from homework2.tasks.hw3 import combinations


@pytest.mark.parametrize(
    ["data1", "data2", "expected_result"],
    [
        (
            [1, 2],
            [3, 4],
            [[1, 3], [1, 4], [2, 3], [2, 4]],
        ),
        ([1], [3, 5], [[1, 3], [1, 5]]),
    ],
)
def test_combinations(data1, data2, expected_result):
    actual_result = combinations(data1, data2)

    assert actual_result == expected_result
