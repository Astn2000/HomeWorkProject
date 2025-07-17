from masks import get_mask_account, get_mask_card_number # type: ignore


def mask_account_card(card_type: str, account_or_card_number: str) -> str:
    """Функция принимает тип счета или карты и его номер , выводит зашифрованный номер"""
    if card_type == "Счет":
        account_number_1 = get_mask_account(account_or_card_number)
        return f"{card_type} {account_number_1}"
    card_number_1 = get_mask_card_number(account_or_card_number)
    return f"{card_type} {get_mask_card_number(card_number_1)}"


def get_date(string_1: str) -> str:
    """Функция принимающая строку , возвращает дату"""
    data = string_1[:10]
    data_corrected = data.split("-")
    return f"{data_corrected[2]}.{data_corrected[1]}.{data_corrected[0]}"


if __name__ == "__main__":
    print(mask_account_card("Счет", "73654108430135874305"))
    print(mask_account_card("Visa Gold", "1234567812345678"))
    print(get_date("2024-03-11T02:26:18.671407"))
