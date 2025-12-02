import json
import os
from typing import Any, List


def read_json_operation(path: str) -> Any:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, List):
                return data

    except (json.JSONDecodeError, IOError):

        return []


print(json.dumps(read_json_operation("C:/Users/Admin/PycharmProjects/PythonProject/PyProject/data/operations.json")))
