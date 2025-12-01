from unittest.mock import patch

from mypy.main import a

from src.external_api import currency_conversion


@patch('requests.get')
def Test_currency_conversion(mock_get):
    transaction_usd = [{"id": 41428829,
                       "state": "EXECUTED",
                       "date": "2019-07-03T18:35:29.512364",
                       "operationAmount": {
                           "amount": "8221.37",
                           "currency": {
                               "name": "USD",
                               "code": "USD"
                           }
                       },
                       "description": "Перевод организации",
                       "from": "MasterCard 7158300734726758",
                       "to": "Счет 35383033474447895560"
                       }]
    mock_get.return_value.json.return_value = {'result': 664694.82125}
    result = currency_conversion(transaction_usd)
    assert result == 664694.82125
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/currency_data/convert?to=RUB&from={a['operationAmount']['currency']['code']}&amount={a['operationAmount']['amount']}")  # noqa: E501
