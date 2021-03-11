import pytest

from homework3.task04.task04 import is_armstrong


def test_negative_number_is_not_armstrong():
    assert is_armstrong(-1) == False


def test_zero_is_armstrong():
    assert is_armstrong(0) == True


def test_poisitve_armstrong_number():
    assert is_armstrong(9) == True


def test_positive_not_armstrong_number():
    assert is_armstrong(10) == False
