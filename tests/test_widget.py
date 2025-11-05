import pytest

from conftest import valid_card_number_2, valid_account_number_2, valid_format_data
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("account_info, expected_result", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Visa 6831982476737658", "Visa 6831 98** **** 7658"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("", "Некорректный номер"),
])
def test_mask_account_card(account_info, expected_result):
    assert mask_account_card(account_info) == expected_result


def test_valid_card_number(valid_card_number_2):  # правильный ввод карты
    assert mask_account_card(valid_card_number_2) == "Visa 1234 56** **** 3456"


def test_valid_card_number_(valid_account_number_2):  # правильный ввод со словом счёт
    assert mask_account_card(valid_account_number_2) == "Счет **9589"


@pytest.mark.parametrize("format_data, expected_result", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2025-06-28T02:26:18.671407", "28.06.2025"),
    ("", "")
])
def test_get_date(valid_format_data):
    assert get_date(valid_format_data) == "11.03.2024"
