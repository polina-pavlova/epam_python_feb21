import pytest

from homework3.task02.task02 import main


def test_sum_for_range_0_501_slow_calculation():
    assert main() == 1025932
