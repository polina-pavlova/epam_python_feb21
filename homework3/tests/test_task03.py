import pytest

from homework3.task03.task03 import make_filter


def test_make_filter():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]
