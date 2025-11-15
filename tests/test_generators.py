import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Transaction in USD",
            "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
        },
        {
            "id": 2,
            "description": "Transaction in EUR",
            "operationAmount": {"amount": "200", "currency": {"name": "EUR", "code": "EUR"}},
        },
        {
            "id": 3,
            "description": "Another USD transaction",
            "operationAmount": {"amount": "150", "currency": {"name": "USD", "code": "USD"}},
        },
    ]


@pytest.mark.parametrize("currency_code, expected_ids", [("USD", [1, 3]), ("EUR", [2]), ("RUB", [])])
def test_filter_by_currency(sample_transactions, currency_code, expected_ids):
    result = list(filter_by_currency(sample_transactions, currency_code))
    result_ids = [tx["id"] for tx in result]
    assert result_ids == expected_ids


def test_filter_by_currency_no_transactions(list_transactions):  # транзакций с заданной валютой нет
    eur_transactions = filter_by_currency(list_transactions, "EUR")
    try:
        next(eur_transactions)
        assert False, "Должно было быть выброшено исключение StopIteration"
    except StopIteration:
        assert True


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    expected_descriptions = ["Transaction in USD", "Transaction in EUR", "Another USD transaction"]
    assert descriptions == expected_descriptions


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (999999999999998, 999999999999999, ["0000 0000 0000 0002", "0000 0000 0000 0003"]),
    ],
)
def test_card_number_generator(start, stop, expected_numbers):
    gen = card_number_generator(start, stop)
    generated_numbers = list(gen)
    assert generated_numbers == expected_numbers


def test_card_number_format():
    gen = card_number_generator(1, 1)
    card_number = next(gen)

    parts = card_number.split()
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 4
        assert part.isdigit()
