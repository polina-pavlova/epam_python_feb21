import pytest

from homework11.tasks.hw2 import Order, Strategy


class MorningDiscount(Strategy):
    def final_price(self):
        return self.price * (1 - 0.5)


class ElderDiscount(Strategy):
    def final_price(self):
        return self.price * (1 - 0.75)


def test_morning_disccount():
    assert Order(100, MorningDiscount).final_price == 50


def test_elder_discount():
    assert Order(100, ElderDiscount).final_price == 25
