import pytest

from homework3.task04.task04 import is_armstrong


@pytest.mark.parametrize(
    ["number", "expected_result"], [(-1, False), (0, True), (9, True), (10, False)]
)
def test_is_armstrong(number, expected_result):
    assert is_armstrong(number) == expected_result
