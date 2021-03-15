"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


>>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import re

import requests


def count_dots_on_i(url: str) -> int:
    try:
        res = requests.get(url)
        counter = 0
        for line in res:
            # line_without_tags = str(re.sub(r'\<[^>]*\>', '', str(line))) #удалить html теги. но в ответе в примере с учетом тегов
            counter += str(line).count("i")
        return counter
    except ValueError:
        print(f"Unreachable {url}")
