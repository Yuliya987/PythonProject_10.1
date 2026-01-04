import re
from typing import Any
from collections import Counter


def process_bank_search(transactions:list[dict], search:str)->list[dict]:
    """
    Фильтрует список операций по наличию подстроки в описании."""
    pattern = re.compile(search, re.IGNORECASE)

    filtered_transactions = [
        op for op in transactions
        if pattern.search(op['description'])
    ]
    return filtered_transactions


def process_bank_operations(transactions:list[dict], categories:list)->dict:
    counter = Counter()
    for op in transactions:
        category = op.get('description', '').strip()
        if category in categories:
            counter[category] += 1
    return dict(counter)
