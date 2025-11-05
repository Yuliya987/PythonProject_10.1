import pytest

from conftest import valid_card_number, valid_account_number
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("account_number, expected_result", [
    ("73654108430135874305", "**4305"),
    ("12479812478964124781", "**4781"),
    ("12345667788991010011", "**0011"),
    ("", "Некорректный номер счёта"),
])
def test_get_mask_account(account_number, expected_result):
    assert get_mask_account(account_number) == expected_result


def test_get_mask_account_len():
    assert len(valid_account_number) == 20


def test_valid_account_number():
    assert get_mask_account(valid_account_number) == "**4305"


def test_account_number_is_missing():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("Счёт")

    assert str(exc_info.value) == "Некорректный номер счёта"


@pytest.mark.parametrize("card_number, expected_result", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1596837868705199", "1596 83** **** 5199"),
    ("", "Некорректный номер карты"),
])
def test_get_mask_card_number(card_number, expected_result):
    assert get_mask_account(card_number) == expected_result


def test_get_mask_card_number_len():
    assert len(valid_card_number) == 16


def test_valid_card_number(valid_card_number):  # правильный ввод с одним словом
    assert get_mask_card_number(valid_card_number) == "7000 79** **** 6361"


def test_card_number_is_missing():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("Visa Classic")

    assert str(exc_info.value) == "Некорректный номер карты"
