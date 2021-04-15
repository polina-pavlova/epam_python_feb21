"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def string_processing(string):
    processed_string = ""
    for char in string:
        if char == "#":
            processed_string = processed_string[:-1]
        else:
            processed_string += char
    return processed_string


def backspace_compare(first: str, second: str):
    return string_processing(first) == string_processing(second)
