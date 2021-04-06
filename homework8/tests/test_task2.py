import pytest

import homework8.tasks.task2 as task2

presidents = task2.TableData(
    database_name="tests/example.sqlite", table_name="presidents"
)


def test_len_method():
    assert len(presidents) == 3


def test_getitem():
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains():
    assert "Trump" in presidents
