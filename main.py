from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

card_number = "7000792289606361"
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
