import json
from typing import Any, List


def read_json_operation(path: str) -> Any:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, List):
                return []
            return data
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []


if __name__ == "__main__":
    print(read_json_operation('C:/Users/Admin/PycharmProjects/PythonProject/PyProject/data/operations.json'))
