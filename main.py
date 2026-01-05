from pathlib import Path
from typing import Callable

from src.csv_reader import csv_transaction, excel_transaction
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search_description import process_bank_search
from src.utils import read_json_operation
from src.widget import get_date, mask_account_card

BASE_DIR = Path(__file__).parent.resolve()

dict_file = {1: read_json_operation, 2: csv_transaction, 3: excel_transaction}
path_file = {1: BASE_DIR / 'data' / 'operations.json',
             2: BASE_DIR / 'data' / 'transactions.csv',
             3: BASE_DIR / 'data' / 'transactions_excel.xls'}

status = ["EXECUTED", "CANCELED", "PENDING"]


def main():
    """Функция, которая отвечает за основную логику проекта"""
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
            print(get_func.__doc__)
            path_: str = path_file.get(user_input)
            transaction = get_func(path_)
            break

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.\n"
              f"Доступные для фильтровки статусы: {', '.join(status)}"
              )
        user_input_status: str = input().upper()
        if user_input_status in status:
            transaction = filter_by_state(transaction, user_input_status)
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

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
    user_input: bool = input().lower() == "да"
    if user_input:
        print("Введите слово для фильтрации: ")
    user_word: str = input()
    transaction = process_bank_search(transaction, user_word)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transaction)}")

    for trans in transaction:
        date = get_date(trans.get("date"))
        amount = trans.get("amount")
        currency_name = trans.get("currency_name")
        to_from = trans.get("from") if isinstance(trans.get("from"), str) else None
        to = mask_account_card(trans.get("to")) if trans.get("to") else None
        description = trans.get("description")

        out_print = f"{date} {description}"
        summ_print = f"Сумма: {amount} {currency_name}"
        check_to = f"{to}"
        check_from = " -> " + mask_account_card(to_from) if to_from else ""
        print(f"{out_print}\n{check_to}{check_from}\n{summ_print}")


if __name__ == "__main__":
    main()
