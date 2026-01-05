import json
import logging
import os
from typing import Any, List

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_operation(path: str) -> Any:
    """Для обработки выбран JSON-файл"""
    if not os.path.exists(path):
        return []
    try:
        logger.info(f"узнаем путь, {path}, к json файлу")
        with open(path, "r", encoding="utf-8") as f:
            data_json = json.load(f)
            data = []
            for transaction in data_json:
                amount = transaction.get("operationAmount", {}).get("amount")
                currency_name = transaction.get("operationAmount", {}).get("currency", {}).get("name")
                currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
                data.append({
                    'id': transaction.get("id"),
                    'state': transaction.get("state"),
                    'date': transaction.get("date"),
                    'amount': amount,
                    'currency_name': currency_name,
                    'currency_code': currency_code,
                    'from': transaction.get("from"),
                    'to': transaction.get("to"),
                    'description': transaction.get("description")
                })
            return data
            if isinstance(data, List):
                return data

    except (json.JSONDecodeError, IOError) as en:
        logger.error(f"Произошла ошибка чтения: {en}")
        return []


print(json.dumps(read_json_operation("C:/Users/Admin/PycharmProjects/PythonProject/PyProject/data/operations.json")))
