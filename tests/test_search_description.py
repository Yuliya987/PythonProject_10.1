import pytest

from src.search_description import process_bank_search, process_bank_operations


@pytest.mark.parametrize(
    "account_number, expected_result",

def test_process_bank_search(

operations = [
    {'id': 1, 'description': 'Пополнение счета на 1000 рублей'},
    {'id': 2, 'description': 'Снятие 5000 с карты'},
    {'id': 3, 'description': 'Перевод на счет 2000'},
    {'id': 4, 'description': 'Оплата услуг связи'}
]
    result = process_bank_search(operations, 'перевод')


print(result)  # Выведет операции с описанием, содержащим слово "перевод"