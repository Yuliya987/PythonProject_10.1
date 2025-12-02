from unittest.mock import patch

from src.external_api import currency_conversion

import requests


@patch("requests.get")
def test_currency_conversion(mock_get, transaction_usd):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 664694.82125}
    result = currency_conversion(transaction_usd)
    assert result == 664694.82125
    mock_get.return_value.status_code = 0
    result = currency_conversion(transaction_usd)
    assert result is None

@patch("requests.get", side_effect=requests.RequestException)
def test_exception(mock_get, transaction_usd):
    result = currency_conversion(transaction_usd)
    assert result is None
