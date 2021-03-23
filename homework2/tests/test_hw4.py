import pytest

from homework2.tasks.hw4 import cache


@pytest.mark.parametrize(
    ["args_1", "args_2", "expected_result"],
    [((2, 3), (2, 3), True), ((2, 3), (3, 4), False)],
)
def test_cache(args_1, args_2, expected_result):
    def func(a, b):
        return (a ** b) ** 2

    actual_result = cache(func)(*args_1) is cache(func)(*args_2)

    assert actual_result == expected_result
