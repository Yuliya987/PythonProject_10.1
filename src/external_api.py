import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def currency_conversion(transaction):
    """Функция конвертирует сумму транзакции в сумму рублях"""

    '''for a in transaction_list:

        if a["operationAmount"]["currency"]["code"] == "RUB":
            return a["operationAmount"]["amount"]

        if a["operationAmount"]["currency"]["code"] != 'RUB':
            response = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?to={a["operationAmount"], ["currency"], ["code"]}&from=a{["operationAmount"], ["currency"], ["code"]}&=a{["operationAmount"], ["amount"]} - {API_KEY}")  # noqa:E501

        return response.json()'''

    url = "https://api.apilayer.com/currency_data/convert"

    operation_amount = transaction["operationAmount"]

    currency_info = operation_amount["currency"]
    currency_code = currency_info["code"]
    amount_value = operation_amount["amount"]

    payload = {"amount": 100, "from": "USD", "to": "RUB"}
    headers = {"apikey": API_KEY}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            result = response.json()
            conversion_result = result.get("result")
            if conversion_result is not None:
                return float(conversion_result)
        return None
    except requests.exceptation.RequestExceptation:
        return None
