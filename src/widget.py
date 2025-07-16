import masks # type: ignore


def mask_account_card(card_type: str, card_number: str) -> str:
    """Функция принимает тип счета или карты и его номер , выводит зашифрованный номер"""
    if card_type != "Счет":
        return f"{card_type} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_type} **{card_number[-4:]}"


def get_date(string_1: str) -> str:
    """Функция принимающая строку , возвращает дату"""
    data = string_1[:10]
    data_corrected = data.split("-")
    return f"{data_corrected[2]}.{data_corrected[1]}.{data_corrected[0]}"


if __name__ == "__main__":
    print(mask_account_card("Visa Gold", "5999414228426353"))
    print(mask_account_card("Счет", "64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(masks.get_mask_card_number(1234567812345678))
    print(masks.get_mask_account(73654108430135874305))
