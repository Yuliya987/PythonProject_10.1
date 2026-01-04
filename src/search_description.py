import re

from main import transactions



'''def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Функция фильтрует словари по состоянию операции: выполнена/отменена"""

    for d in data:
        try:
            pattern = re.compile(r"EXECUTED")
            re.findall(pattern, search, flags=0)
            matches = pattern.search(d)
            return matches
        except Exception as e:
            return e'''


def process_bank_search(operations:list[dict], search:str)->list[dict]:
    """
    Фильтрует список операций по наличию подстроки в описании.

    :param operations: список словарей с банковскими операциями
    :param search: строка для поиска в описании операций
    :return: отфильтрованный список операций
    """
    pattern = re.compile(search, re.IGNORECASE)

    filtered_operations = [
        op for op in operations
        if pattern.search(op['description'])
    ]

    return filtered_operations


# Пример использования:
operations = [
    {'id': 1, 'description': 'Пополнение счета на 1000 рублей'},
    {'id': 2, 'description': 'Снятие 5000 с карты'},
    {'id': 3, 'description': 'Перевод на счет 2000'},
    {'id': 4, 'description': 'Оплата услуг связи'}
]

result = filter_operations_by_description(operations, 'перевод')
print(result)  # Выведет операции с описанием, содержащим слово "перевод"