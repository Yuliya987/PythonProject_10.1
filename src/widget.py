from src.masks import get_mask_account, get_mask_card_number


account_info = input("Введите тип и номер карты или счета: ")


def mask_account_card(account_info: str) ->str:
    """Маскирует номер карты или счета, представленного в виде строки."""


    parts = account_info.split()  # Делим входящюю информацию на части
    account_type = ' '.join(parts[:-1])  # Объединяем все слова, кроме последнего
    account_number = parts[-1]
    if account_info.startswith("Счет"):
        masked_account = get_mask_account(account_number)
        return f"Счет {masked_account}"
    else:
        card_number = account_number
        masked_card = get_mask_card_number(card_number)
        return f"{account_type} {masked_card}"


account_info = "Maestro 1596837868705199"
mask_account_card(account_info)


def get_date(format_data: str) ->str:
    '''Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ"'''
    new_data = format_data[8:10] + "." + format_data[5:7] + "." + format_data[0:4]
    return new_data
