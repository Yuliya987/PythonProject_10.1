import json
import logging
import os
from typing import Any, List

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_formater.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_operation(path: str) -> Any:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(path):
        return []
    try:
        logger.info(f"узнаем путь, {path}, к json файлу")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, List):
                return data

    except (json.JSONDecodeError, IOError) as en:
        logger.error(f"Произошла ошибка чтения: {en}")
        return []


print(json.dumps(read_json_operation("C:/Users/Admin/PycharmProjects/PythonProject/PyProject/data/operations.json")))
