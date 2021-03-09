import pytest

from homework2.tasks.hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (
            [3, 2, 3],
            (3, 2),
        ),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ],
)
def test_major_and_minor_elem(data, expected_result):
    actual_result = major_and_minor_elem(data)

    assert actual_result == expected_result
