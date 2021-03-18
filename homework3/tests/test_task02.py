import pytest

from homework3.task02.task02 import parallel_calculation


def test_sum_for_range_0_501_slow_calculation():
    assert parallel_calculation() == 1025932
