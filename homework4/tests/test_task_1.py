from unittest import mock

import pytest

from homework4.tasks.task_1_read_file import read_magic_number


def test_positive_case():
    mock_open = mock.mock_open(read_data="1\n23")
    with mock.patch("builtins.open", mock_open):
        result = read_magic_number(mock_open)
        assert result == True


def test_negative_case_bottom_boundary():
    mock_open = mock.mock_open(read_data="0.99\n23")
    with mock.patch("builtins.open", mock_open):
        result = read_magic_number(mock_open)
        assert result == False


def test_negative_case_upper_boundary():
    mock_open = mock.mock_open(read_data="3\n23")
    with mock.patch("builtins.open", mock_open):
        result = read_magic_number(mock_open)
        assert result == False


def test_negative_value_error():
    mock_open = mock.mock_open(read_data="abc\ndsh")
    with pytest.raises(ValueError):
        with mock.patch("builtins.open", mock_open):
            read_magic_number(mock_open)
        assert ValueError
