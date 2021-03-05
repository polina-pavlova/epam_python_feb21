from typing import List

import pytest

from homework1.tasks.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        (
            [0, 1, 2, 3, 4, 5],
            [-5, -4, -3, -2, -1, 0],
            [5, 4, 3, 2, 1, 0],
            [6, -1, -1, -3, 4, -5],
            3,
        ),
        ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 4),
        ([-1, -1], [0, 0], [0, 0], [1, 1], 2),
    ],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
