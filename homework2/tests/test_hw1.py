import pytest

from homework2.tasks.hw1 import *


def test_get_longest_diverse_words():
    assert get_longest_diverse_words("tests/data.txt") == [
        "politisch-strategischen",
        "Verfassungsverletzungen",
        "Souveränitätsansprüche",
        "Mehrheitsvorstellungen",
        "zoologisch-politischen",
        "Wiederbelebungsübungen",
        "Werkstättenlandschaft",
        "résistance-Bewegungen",
        "Entscheidungsschlacht",
        "politisch-technischen",
    ]


def test_get_rarest_char():
    assert get_rarest_char("tests/data.txt") == ["›", "‹", "Y", "î", "’", "X", "(", ")"]


def test_count_punctuation_chars():
    assert count_punctuation_chars("tests/data.txt") == {
        "'": 3,
        "(": 1,
        ")": 1,
        ",": 2489,
        "-": 1016,
        ".": 1615,
        ":": 79,
        ";": 73,
        "?": 28,
        "«": 43,
        "»": 43,
        "‹": 1,
        "›": 1,
    }


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("tests/data.txt") == {
        "Ü": 42,
        "»": 43,
        "«": 43,
        "—": 81,
        "ß": 708,
        "ü": 804,
        "ä": 866,
        "ö": 357,
        "›": 1,
        "‹": 1,
        "Ä": 15,
        "Ö": 3,
        "é": 6,
        "î": 1,
        "’": 1,
    }


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("tests/data.txt") == "ä"
