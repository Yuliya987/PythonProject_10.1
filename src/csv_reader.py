import csv
from pathlib import Path
from typing import Any, List, Dict

import pandas as pd
from pandas import DataFrame
import os


base_dir = os.getcwd()
file_path = os.path.join(base_dir, 'data', 'transaction.csv')

def csv_transaction(file_path: str) -> List[Dict[str, Any]]:
    """Для обработки выбран CSV-файл"""
    reader_scv_list = []
    try:
        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                reader_scv_list.append(row)
            return reader_scv_list
    except FileNotFoundError:
        return []


file_path_ = os.path.join(base_dir, 'data', 'transactions_excel.xlsx')

def excel_transaction(file_path_: str) -> List[Dict[str, Any]]:
    """Для обработки выбран Excel-файл"""
    try:
        excel_data: DataFrame = pd.read_excel(file_path_)
        excel_data.notnull()
        transaction_list = excel_data.to_dict(orient="records")
        return transaction_list
    except FileNotFoundError:
        return []
