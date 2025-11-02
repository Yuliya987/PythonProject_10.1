from src.masks import get_mask_account, get_mask_card_number

from src.widget import mask_account_card, get_date

card_number = "7000792289606361"
get_mask_card_number(card_number)

account_number = "73654108430135874305"
get_mask_account(account_number)

account_info = "Maestro 1596837868705199"
mask_account_card(account_info)

format_data = "2024-03-11T02:26:18.671407"
get_date(format_data)

