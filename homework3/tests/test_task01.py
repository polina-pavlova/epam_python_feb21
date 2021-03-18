from unittest import mock

import pytest
from mock import Mock

from homework3.task01.task01 import cache

mock_func = Mock()


def test_in_cache():
    cached = cache(3)(mock_func)
    cached(1, 2)
    cached(1, 2)
    assert mock_func.call_count == 1


def test_not_in_cache():
    cached = cache(3)(mock_func)
    cached(1, 2)
    cached(1)
    assert mock_func.call_count == 3
