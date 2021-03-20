from unittest import mock

import pytest

from homework4.tasks.task_1_read_file import read_magic_number


@pytest.mark.parametrize(
    ["file_input", "expected_result"],
    [
        ("1\n23", True),
        ("0.99\n233", False),
        ("3\n23", False),
    ],
)
def test_intervals(file_input, expected_result):
    mock_open = mock.mock_open(read_data=file_input)
    with mock.patch("builtins.open", mock_open):
        result = read_magic_number(mock_open)
        assert result == expected_result


def test_value_error():
    mock_open = mock.mock_open(read_data="abc\ndsh")
    with pytest.raises(ValueError):
        with mock.patch("builtins.open", mock_open):
            read_magic_number(mock_open)
        assert ValueError
