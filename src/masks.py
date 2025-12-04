import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_formater.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты."""
    card_number = card_number.strip()
    logger.warning("Номер карты должен содержать 16 цифр")
    if len(card_number) != 16 or not card_number.isdigit():
        return "Некорректный номер карты"
    first_block = card_number[:4]
    second_block = card_number[4:6]
    last_block = card_number[-4:]
    logger.info("Маскировка номера карты")
    return f"{first_block} {second_block}** **** {last_block}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета."""
    account_number = account_number.strip()
    logger.warning("Номер счета должен содержать 20 цифр")
    if len(account_number) != 20 or not account_number.isdigit():
        return "Некорректный номер счёта"
    last_four = account_number[-4:]
    logger.info("Маскировка номера счета")
    return f"**{last_four}"
