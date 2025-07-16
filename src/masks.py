from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскирующая часть номера карты"""
    card_number = str(card_number)
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскирующая номер счета"""
    account_number = str(account_number)
    return f"**{account_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(1234567812345678))
    print(get_mask_account(73654108430135874305))
