import json
import os
from src.external_api import currency_conversion
from typing import List, Any

from dotenv.main import logger
from jaraco.functools import except_
from requests import Response


def read_json_operation(path: str) -> Any:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r', encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, List):
                return data

    except (json.JSONDecodeError, IOError):

        return []

def get_transaction_amount(transaction: dict[str, Any])-> float| None| Response |Any:
    """Возвращает сумму транзакции в рублях"""
    logger.debug("Starting transaction amount processing")

    try:
        operation_amount = transaction.get("operationAmount", {})

        if not operation_amount:
            logger.info("No operationAmount found in transaction")
            return 0.0

        currency_info = operation_amount.get("currency", {})
        currency_code = currency_info.get("code")
        amount_value = operation_amount.get("amount")

        if not currency_code or not amount_value:
            return 0.0

        if currency_code == "RUB":
            logger.debug(f"Transaction is RUB, returning amount {amount_value}")
            return amount_value

        logger.info(f"Converting transaction from {currency_code} to RUB")
        converted_amount = currency_conversion(transaction)

        if converted_amount is not None:
            logger.debug(f"Successfully converted amount: {converted_amount} RUB")
            return converted_amount

        else:
            logger.warning(f"Currency conversion failed for {currency_code}")
            return 0.0

    except (ValueError, TypeError) as ex:
        logger.error(ex)
        return 0.0

print(json.dumps(read_json_operation('C:/Users/Admin/PycharmProjects/PythonProject/PyProject/data/operations.json')))
