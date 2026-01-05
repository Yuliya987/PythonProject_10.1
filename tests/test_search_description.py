import pytest

from src.search_description import process_bank_search, process_bank_operations


@pytest.mark.parametrize(
    "search_, expected_result",
    [
        ("перевод", [{'description': 'Перевод на счет 2000', 'id': 3 }]),
        ("оплата", [{'description': 'Оплата услуг связи', 'id': 4}]),
        ("пополнение", [{'description': 'Пополнение счета на 1000 рублей', 'id': 1}]),
        ("снятие", [{'description': 'Снятие 5000 с карты', 'id': 2}]),
    ],
)


def test_process_bank_search(transactions_1, search_, expected_result):
    assert process_bank_search(transactions_1, search_) == expected_result


def test_process_bank_operations(transactions_1):
    result = process_bank_operations(transactions_1, categories=["Перевод на счет 2000"])
    assert result == {"Перевод на счет 2000": 1}
