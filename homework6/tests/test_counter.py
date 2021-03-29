import pytest

from homework6.tasks.counter import instances_counter


@instances_counter
class User:
    pass


def test_get_created_instances_zero_instances():
    assert User.get_created_instances() == 0


def test_get_created_instances_few_instances():
    user, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3


def test_reset_instances_counter():
    assert User.reset_instances_counter() == 3


def test_reset_instances_counter_after_reset():
    user, _, _ = User(), User(), User()
    User.reset_instances_counter()
    assert User.reset_instances_counter() == 0
