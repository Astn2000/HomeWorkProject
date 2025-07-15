from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскирующая часть номера карты"""
    card_number = str(card_number)
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскирующая номер счета"""
    account_number = str(account_number)
    return f"**{account_number[-4:]}"


def mask_account_card(card_type: str, card_number: str) -> str:
    """ Функция принимает тип счета или карты и его номер , выводит зашифрованный номер """
    if card_type != "Счет":
        return f"{card_type} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_type} **{card_number[-4:]}"


def get_date(string_1: str) -> str:
    """ Функция принимающая строку , возвращает дату """
    data = string_1[:10]
    data_corrected = data.split("-")
    return f"{data_corrected[2]}.{data_corrected[1]}.{data_corrected[0]}"


if __name__ == "__main__":
    print(get_mask_card_number(1234567812345678))
    print(get_mask_account(73654108430135874305))
