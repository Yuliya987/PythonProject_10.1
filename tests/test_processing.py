from src.processing import filter_by_state, sort_by_date

def test_filter_by_state
    assert

def test_sort_by_date
    assert

def test_filter_by_state_executed() -> None:
    transactions = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    expected = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(transactions) == expected

def test_sort_by_date_growing(transaction_data) -> None:  # Проверяем сортировку по возрастанию
    sorted_transactions = sort_by_date(transaction_data, descending=False)
    assert sorted_transactions[0]["id"] == 4  # Самая ранняя дата должна быть первой
    assert sorted_transactions[1]["id"] == 2
    assert sorted_transactions[2]["id"] == 3
    assert sorted_transactions[3]["id"] == 1