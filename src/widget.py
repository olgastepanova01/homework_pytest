from datetime import datetime
from typing import Any

import masks

# from src.masks import get_mask_account


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
            mask_card = masks.get_mask_account(digit_card)
        return f"{alpha_card} {mask_card}"
    return None


# print(mask_account_card("Visa Platinum 7000792289606361"))
# print(mask_account_card("Счет 73654108430135874305"))


def get_date(input_time: str) -> str:
    """Функция get_date принимает на вход строку и отдает корректный результат в формате ДД.ММ.ГГГГ"""
    date_obj = datetime.strptime(input_time, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


# print(get_date("2024-03-11T02:26:18.671407"))
