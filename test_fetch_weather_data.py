"""
testing capabilities for fetch_weather_data.py
"""
# test fetch_weather_data.py
import pytest
from requests import JSONDecodeError

import fetch_weather_data


def test_pytest():
    """
    pytest testing, just for github actions
    :return: None
    """
    print("Test called successfully!")
    assert True


def test_fetch_weather_data():
    """
    test error handling of the fetch weather data func
    :return: None
    """
    with pytest.raises(JSONDecodeError):
        fetch_weather_data.fetch_weather_data("https://www.google.com")
