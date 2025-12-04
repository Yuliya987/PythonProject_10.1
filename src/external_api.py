import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction):
    """Функция конвертирует сумму транзакции в сумму рублях"""

    operation_amount = transaction["operationAmount"]

    currency_info = operation_amount["currency"]
    currency_code = currency_info["code"]
    amount_value = operation_amount["amount"]

    url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency_code}&amount={amount_value}"

    payload = {}
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code == 200:
            result = response.json()
            conversion_result = result.get("result")
            if conversion_result is not None:
                return float(conversion_result)
        return None
    except requests.RequestException:
        return None
