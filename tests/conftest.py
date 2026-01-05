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
def list_dict_1():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def transaction_usd():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


@pytest.fixture
def transactions_1():
    return [
        {'description': 'Пополнение счета на 1000 рублей', 'id': 1},
        {'description': 'Снятие 5000 с карты', 'id': 2},
        {'description': 'Перевод на счет 2000', 'id': 3 },
        {'description': 'Оплата услуг связи', 'id': 4}
    ]
