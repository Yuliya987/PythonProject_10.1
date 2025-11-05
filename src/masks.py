def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты."""
    card_number = card_number.strip()
    if len(card_number) != 16 or not card_number.isdigit():
        return "Некорректный номер карты"
    first_block = card_number[:4]
    second_block = card_number[4:6]
    last_block = card_number[-4:]
    return f"{first_block} {second_block}** **** {last_block}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета."""
    account_number = account_number.strip()
    if len(account_number) != 20 or not account_number.isdigit():
        return "Некорректный номер счёта"
    last_four = account_number[-4:]
    return f"**{last_four}"
