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

@pytest.fixture
def list_dict_1():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
