from typing import Dict, Iterator, List


def filter_by_currency(list_transactions: List, currency: str) -> Iterator:
    """Функция возвращает итератор по операциям по заданной валюте"""
    for transaction in (t for t in list_transactions if t["operationAmount"]["currency"]["name"] == currency):
        yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator:
    """Генератор, возвращающий описание каждой транзакции."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генератор номеров карт в диапазоне [start, end]."""
    for num in range(start, stop + 1):
        num_str = f"{num:016d}"
        formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted_number
