from inspect import isfunction

import pytest

import homework5.tasks.save_original_info as orig_info


@orig_info.print_result
def func_for_testing(a):
    """Add 1 to a number"""
    return a + 1


def test_func_for_testing():
    assert func_for_testing(3) == 4


def test_doc():
    assert func_for_testing.__doc__ == "Add 1 to a number"


def test_name():
    assert func_for_testing.__name__ == "func_for_testing"


def test_original_func():
    func = func_for_testing.__original_func
    assert isfunction(func)


def test_orig_func_calculation():
    func = func_for_testing.__original_func
    assert func(2) == func_for_testing(2)
