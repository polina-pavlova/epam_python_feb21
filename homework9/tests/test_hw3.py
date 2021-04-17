import pytest

from homework9.tasks.hw3 import universal_file_counter


def test_none_tokenizer():
    assert universal_file_counter("./tests", "txt") == 12


def test_add_tokenizer():
    assert universal_file_counter("./tests", "txt", str.split) == 12
