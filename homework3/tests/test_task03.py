import pytest

import homework3.task03.task03 as filt

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


def test_non_empty_result_of_make_filter():
    # assert make_filter(name="polly", type="bird").func(sample_data) == [
    #     {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    # ]
    assert filt.Filter.func(
        sample_data, filt.make_filter(name="polly", type="bird")
    ) == [{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}]


def test_empty_result_of_make_filter():
    # assert (
    #     make_filter(name="polly", type="bird", last_name="test").func(sample_data) == []
    # )
    assert (
        filt.Filter.func(
            sample_data, filt.make_filter(name="polly", type="bird", last_name="test")
        )
        == []
    )
