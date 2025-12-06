import csv
from typing import Any

import pandas as pd

file_path_csv = "C:/Users/Admin/PycharmProjects/PythonProject/transactions.csv"


def csv_transaction(file_path_csv: str) -> Any:
    """Функция для чтения csv-файла, выдает список словарей с транзакциями"""
    try:
        with open("transactions.csv") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                print(
                    row["id"],
                    row["state"],
                    row["date"],
                    row["amount"],
                    row["currency_name"],
                    row["currency_code"],
                    row["from"],
                    row["to"],
                    row["description"],
                )
    except FileNotFoundError:
        return []


file_path = "C:/Users/Admin/PycharmProjects/PythonProject/transactions_excel.xlsx"


def excel_transaction(file_path: str) -> Any:
    """Функция для чтения Excel-файла, выдает список словарей с транзакциями"""
    try:
        excel_data = pd.read_excel("transactions_excel.xlsx", sheet_name=None)
    except FileNotFoundError:
        return []
    return excel_data
