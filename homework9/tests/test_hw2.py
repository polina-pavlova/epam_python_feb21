import pytest

from homework9.tasks.hw2 import Suppressor, suppressor


def test_generator_suppressor():
    assert suppressor(IndexError)


def test_class_suppressor():
    assert Suppressor(KeyError)


def test_generator_suppressor_break():
    with pytest.raises(IndexError):
        with suppressor(KeyError):
            raise IndexError


def test_class_suppressor_break():
    with pytest.raises(IndexError):
        with Suppressor(KeyError):
            raise IndexError
