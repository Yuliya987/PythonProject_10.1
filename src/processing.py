def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция которая возвращает новый список словарей в соответствии с аргументом state (по умолчанию - EXECUTED)"""
    new_list_dict = []

    for sta in list_dict:
        if sta.get("state") == state:
            new_list_dict.append(sta)

    return new_list_dict


def sort_by_date(list_dict: list[dict], sort_reverse: bool = True) -> list[dict]:
    """Функция сортировки списка словарей по дате (по умолчанию - убывание)"""
    sorted_list_dict = sorted(list_dict, key=lambda x: x["date"], reverse=sort_reverse)

    return sorted_list_dict
