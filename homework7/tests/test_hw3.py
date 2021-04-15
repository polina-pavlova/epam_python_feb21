import pytest

from homework7.tasks.hw3 import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        ([["x", "o", "o"], ["o", "o", "x"], ["x", "x", "o"]], "draw!"),
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished"),
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "x", "x"]], "x wins!"),  # test rows
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "x", "o"]], "o wins!"),  # test cols
        (
            [["-", "-", "o"], ["-", "o", "o"], ["o", "o", "x"]],
            "o wins!",
        ),  # test anti-main diagonal
        (
            [["x", "-", "o"], ["-", "x", "o"], ["-", "x", "x"]],
            "x wins!",
        ),  # test main diag
        ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], "unfinished"),
    ],
)
def test_tic_tac_toe_checker(board, expected_result):
    assert tic_tac_toe_checker(board) == expected_result
