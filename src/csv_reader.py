import csv
from typing import Any, List, Dict

import pandas as pd

file_path_csv = "C:/Users/Admin/PycharmProjects/PythonProject/transactions.csv"


def csv_transaction(file_path_csv: str) -> List[Dict[str, Any]]:
    """Для обработки выбран CSV-файл"""
    try:
        with open("transactions.csv") as file:
            reader = csv.DictReader(file, delimiter=";")
            transactions = []
            for row in reader:
                transactions.append(row)
            return transactions
    except FileNotFoundError:
        return []


file_path = "C:/Users/Admin/PycharmProjects/PythonProject/transactions_excel.xlsx"


def excel_transaction(file_path: str) -> List[Dict[str, Any]]:
    """Для обработки выбран Excel-файл"""
    try:
        excel_data = pd.read_excel(file_path)
        transaction_list = excel_data.to_dict(orient="records")
        return transaction_list
    except FileNotFoundError:
        return []
