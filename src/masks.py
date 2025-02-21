from typing import Union


def get_mask_card_number(card_number: Union[str | int]) -> str | None:
    """Функция get_mask_card_number принимает на вход номер карты, проверяет количество символов"""
    card_number_str = str(card_number)
    if card_number_str == card_number_str.isdigit() or len(card_number_str) == 16:
        return f"{card_number_str[:4]} {card_number_str[4:6]} {'*' * 2} {'*' * 4} {card_number_str[-4:]}"
    else:
        return None


#print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: Union[str | int]) -> str | None:
    """Функция get_mask_account принимает на вход номер счета, проверяет количество символов"""
    account_number_str = str(account_number)
    if account_number_str == account_number_str.isdigit() or len(account_number_str) == 20:
        return f"**{account_number_str[-4:]}"
    else:
        return None


#print(get_mask_account("73654108430135874305"))
