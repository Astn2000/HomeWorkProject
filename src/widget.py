def mask_account_card(card_type: str, card_number: str) -> str:
     if card_type != 'Счет':
        return f"{card_type} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
     return f"{card_type} **{card_number[-4:]}"


def get_date(string_1: str) -> str:
    data = string_1[:10]
    data_corrected = data.split('-')
    return f'{data_corrected[2]}.{data_corrected[1]}.{data_corrected[0]}'



print(mask_account_card('Visa Gold', '5999414228426353'))
print(mask_account_card('Счет', '64686473678894779589'))
print(get_date("2024-03-11T02:26:18.671407"))
