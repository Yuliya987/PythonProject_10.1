import pytest

from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import valid_card_number


@pytest.mark.parametrize(
    "account_number, expected_result",
    [
        ("73654108430135874305", "**4305"),
        ("12479812478964124781", "**4781"),
        ("12345667788991010011", "**0011"),
        ("", "Некорректный номер счёта"),
    ],
)
def test_get_mask_account(account_number, expected_result):
    assert get_mask_account(account_number) == expected_result


@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("", "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result


def test_valid_card_number(valid_card_number):  # правильный ввод с одним словом
    assert get_mask_card_number(valid_card_number) == "7000 79** **** 6361"
