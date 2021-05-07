import pytest

from homework11.tasks.hw2 import Order


def morning_discount(order):
    return order.price * (1 - 0.5)


def elder_discount(order):
    return order.price * (1 - 0.75)


def test_morning_disccount():
    assert Order(100, morning_discount).final_price() == 50


def test_elder_discount():
    assert Order(100, elder_discount).final_price() == 25
