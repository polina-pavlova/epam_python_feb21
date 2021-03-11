from typing import List

import pytest

from homework1.tasks.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([0, 1, 2], [1, 2, 3], [3, 4, 5], [1, 2, 3], 0),
        ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 256),
        ([-1, -1], [0, 0], [0, 0], [1, 1], 16),
    ],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
