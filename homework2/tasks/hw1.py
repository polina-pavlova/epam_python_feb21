"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import defaultdict
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    words = {}
    with open(file_path, encoding="unicode-escape") as fi:
        for line in fi:
            if line.endswith("-\n"):
                line = line.strip("-\n") + fi.readline()
            words_in_line = line.split()
            words_in_line = [
                word.strip(string.punctuation + "«»‹›") for word in words_in_line
            ]
            for word in words_in_line:
                words[word] = [len(word), len(set(word))]
    return [word for word in sorted(words, key=words.get, reverse=True)][:10]


def get_rarest_char(file_path: str):
    chars = defaultdict(int)
    with open(file_path, encoding="unicode-escape") as fi:
        for char in list(fi.read()):
            chars[char] += 1
    rarest_frequency = min(chars.values())
    return [char for char in chars if chars[char] == rarest_frequency]


def count_punctuation_chars(file_path: str):
    punctuation_chars = dict.fromkeys(string.punctuation + "«»‹›", 0)
    with open(file_path, encoding="unicode-escape") as fi:
        for char in list(fi.read()):
            if char in punctuation_chars:
                punctuation_chars[char] += 1
    return {key: value for key, value in punctuation_chars.items() if value != 0}


def count_non_ascii_chars(file_path: str) -> int:
    non_ascii_chars = {}
    with open(file_path, encoding="unicode-escape") as fi:
        for char in list(fi.read()):
            if not char.isascii():
                if char in non_ascii_chars:
                    non_ascii_chars[char] += 1
                else:
                    non_ascii_chars[char] = 1
    return non_ascii_chars


def get_most_common_non_ascii_char(file_path: str) -> str:
    non_ascii_chars_counts = count_non_ascii_chars(file_path)
    return sorted(non_ascii_chars_counts, key=non_ascii_chars_counts.get, reverse=True)[
        0
    ]
