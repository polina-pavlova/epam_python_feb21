"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def count_tokens(file, tokenizer: Optional[Callable] = None):
    counter = 0
    if tokenizer:
        with open(file, "r") as fi:
            for _ in tokenizer(fi.read()):
                counter += 1
    else:
        with open(file, "r") as fi:
            for _ in fi.readlines():
                counter += 1
    return counter


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    files_list = Path(dir_path).rglob(f"*.{file_extension}")
    counter = 0
    for file in files_list:
        counter += count_tokens(file, tokenizer)
    return counter
