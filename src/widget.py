from datetime import datetime
from typing import Any, Union


def get_mask_account(account_number: Union[str, int]) -> str | None:
    """Функция get_mask_account принимает на вход номер счета, проверяет количество символов"""
    account_number_str = str(account_number)
    if account_number_str.isdigit() and len(account_number_str) == 20:
        return f"**{account_number_str[-4:]}"
    else:
        return None


def mask_account_card(mask_card: Any) -> str | None:
    """Функция mask_account_card принимает на вход тип и номер карты или номер счета и возвращает в формате маску"""
    alpha_card = ""
    digit_card = ""
    list_mask_card = mask_card.split()
    if "Maestro" in list_mask_card or "Visa" in list_mask_card:
        mask_card = []
        for i in list_mask_card:
            if i.isalpha():
                mask_card = " ".join(list_mask_card[:-1])
            elif i.isdigit():
                digit_card = i
        return f"""{"".join(mask_card)} {digit_card[0:4]} {digit_card[4:6]}** **** {digit_card[-4:]}"""
    elif "Счет" in list_mask_card:
        for i in list_mask_card:
            if i.isalpha():
                alpha_card += i
            elif i.isdigit():
                digit_card += i
            mask_card = get_mask_account(digit_card)  # Используем локальную функцию
        return f"{alpha_card} {mask_card}"
    return None


# Примеры использования
print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Счет 73654108430135874305"))       # Счет **4305


def get_date(input_time: str) -> str:
    """Функция get_date принимает на вход строку и отдает корректный результат в формате ДД.ММ.ГГГГ"""
    date_obj = datetime.strptime(input_time, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


# print(get_date("2024-03-11T02:26:18.671407"))
