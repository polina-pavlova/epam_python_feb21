from unittest import mock

import pytest
from mock import Mock

from homework3.task01.task01 import cache


def func_for_testing():
    return 1


def test_in_cache():
    with mock.patch("func_cache", autospec=True) as patched_cache:
        cache(times=2)(func_for_testing)
    patched_cache.assert_has_calls()
