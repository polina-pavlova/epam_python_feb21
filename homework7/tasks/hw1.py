"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0

    if tree == element:
        counter += 1

    elif isinstance(tree, (list, tuple, set)):
        for i in tree:
            counter += find_occurrences(i, element)

    elif isinstance(tree, dict):
        for k, v in tree.items():
            if k == element:
                counter += 1
            counter += find_occurrences(v, element)

    return counter


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
