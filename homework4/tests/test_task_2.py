from unittest import mock

import pytest
import requests_mock

from homework4.tasks.task_2_mock_input import count_dots_on_i


def test_i_is_on_page():
    with requests_mock.Mocker() as mock_url:
        mock_url.register_uri("GET", "http://test.com", text="wind")
        actual_result = count_dots_on_i("http://test.com")
        assert actual_result == 1


def test_i_is_not_on_page():
    with requests_mock.Mocker() as mock_url:
        mock_url.register_uri("GET", "http://test.com", text="water")
        actual_result = count_dots_on_i("http://test.com")
        assert actual_result == 0


def test_value_error():
    def raise_value_error(url):
        raise ValueError(f"Unreachable {url}")

    with pytest.raises(ValueError):
        with mock.patch("requests.get", raise_value_error):
            count_dots_on_i("http://test_wrong.com")
