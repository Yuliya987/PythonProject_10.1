from pathlib import Path
from typing import Callable

from src.csv_reader import csv_transaction, excel_transaction
from src.generators import filter_by_currency
from src.masks import get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.search_description import process_bank_search
from src.utils import read_json_operation
from src.widget import get_date

'''card_number = "7000792289606361"
get_mask_card_number(card_number)

account_number = "73654108430135874305"
get_mask_account(account_number)

account_info = "Maestro 1596837868705199"
mask_account_card(account_info)

format_data = "2024-03-11T02:26:18.671407"
get_date(format_data)

list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
filter_by_state(list_dict)

sort_by_date(list_dict)

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]
currency = "USD"
filter_by_currency(transactions, currency)


transactions_1 = [
        {'id': 1, 'description': 'Пополнение счета на 1000 рублей'},
        {'id': 2, 'description': 'Снятие 5000 с карты'},
        {'id': 3, 'description': 'Перевод на счет 2000'},
        {'id': 4, 'description': 'Оплата услуг связи'}
    ]
search_ = "перевод"
process_bank_search(transactions_1, search_)


transaction_descriptions(transactions)


filename = "mylog.txt"
log(filename)'''

BASE_DIR = Path(__file__).parent.resolve()


dict_file = {1: read_json_operation, 2: csv_transaction, 3: excel_transaction}
path_file = {1: BASE_DIR / 'data' / 'operations.json',
             2: BASE_DIR / 'data' / 'transactions.csv',
             3: BASE_DIR / 'data' / 'transactions_excel.xls'}

status = ["EXECUTED", "CANCELED", "PENDING"]


def main():
    while True:
        print(
            "Привет! Привет! Добро пожаловать в программу работы с банковскими транзакциями."
            "Выберите необходимый пункт в меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла.\n"
            "2. Получить информацию о транзакциях из CSV-файла.\n"
            "3. Получить информацию о транзакциях из XLSX-файла.\n"
        )
        user_input: int = int(input())
        get_func: Callable | None = dict_file.get(user_input)
        if get_func:
            path_: str = path_file.get(user_input)
            transaction = get_func(path_)
            break

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.\n"
              f"Доступные для фильтровки статусы: {', '.join(status)}"
              )
        user_input_status: str = input().upper()
        if user_input_status in status:
            transaction1 = filter_by_state(transaction, user_input_status)
            print(f"Операции отфильтрованы по статусу {user_input_status}")
            break
        else:
            print(f"Операции {user_input_status} недоступны")

    print("Отсортировать операции по дате? Да / Нет")
    user_input: bool = input().lower() == "да"
    if user_input:
        print("Отсортировать по возрастанию или по убыванию?")
    user_sort_reverse: bool = input().lower() == "по убыванию"
    transaction = sort_by_date(transaction, user_sort_reverse)

    print("Выводить только рублевые транзакции? Да / Нет ")
    user_input: bool = input().lower() == "да"
    if user_input:
        transaction = filter_by_currency(transaction, "RUB")
    print(transaction)

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
    user_input: bool = input().lower() == "да"
    if user_input:
        print("Введите слово для фильтрации: ")
    user_word: str = input()
    transaction = process_bank_search(transaction, user_word)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transaction)}")

    for trans in transaction:
        state = trans.get("state")
    date = get_date.trans.get("date")
    amount = trans.get("amount")
    currency_name = trans.get("currency_name")
    currency_code = trans.get("currency_code")
    to_from = get_mask_card_number(trans.get("from")) if isinstance(trans.get("from"), str) else None
    to = get_mask_card_number(trans.get("to")) if trans.get("to") else None
    description = trans.get("description")

    out_print = f"{"date"}{description}"
    summ_print = f"Сумма: {amount} {currency_name}"
    check_to = f"{to}"
    check_from = " -> " + get_mask_card_number(to_from) if to_from else ""
    print(f"{out_print}\n{check_to}{check_from}\n{summ_print}")


if __name__ == "__main__":
    main()
