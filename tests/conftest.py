import pytest

@pytest.fixture

def valid_card_number():
    return "7000792289606361"

@pytest.fixture

def valid_card_number_2():
    return "Visa Classic 1234567890123456"

@pytest.fixture
def valid_account_number():
    return "73654108430135874305"

@pytest.fixture
def valid_account_number_2():
    return "Счет 64686473678894779589"

@pytest.fixture
def valid_format_data():
    return "2024-03-11T02:26:18.671407"