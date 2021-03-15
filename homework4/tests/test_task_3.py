import pytest

from homework4.tasks.task_3_get_print_output import my_precious_logger


def test_stderr(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"


def test_stdout(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK"
