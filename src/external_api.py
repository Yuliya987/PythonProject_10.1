import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')


def transaction_info(transaction_list):
    """Функция, принимающая транзакцию и возвращающая сумму транзакции в рублях"""

    for i in transaction_list:

        if i["operationAmount"]["currency"]["code"] == "RUB":
            return i["operationAmount"]["amount"]

        if i["operationAmount"]["currency"]["code"] != 'RUB':
            response = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?to=i,{["operationAmount"]},{["currency"]},{["code"]}&from=i{["operationAmount"]},{["currency"]},{["code"]}&=i{["operationAmount"]},{["amount"]} - {API_KEY}")  # noqa:E501

        return response.json()
