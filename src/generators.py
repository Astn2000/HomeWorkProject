from typing import Any, Generator


def filter_by_currency(transactions: list, currency: str = "USD") -> Any | None:
    """Функция обрабатывающая список транзакций выводит транзакции с указанной валютой"""
    for transaction in transactions:
        currency_name = transaction["operationAmount"]["currency"]["name"]
        if currency_name == currency:
            print(transaction)
    return ""


print(
    filter_by_currency(
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
        ],
        "RUB"
    )
)


def transaction_descriptions(transactions: list) -> str:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции"""
    for transaction in transactions:
        description_name = transaction["description"]
        print(description_name)
    return ''


print(
    transaction_descriptions(
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
{
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2019-01-20T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2017-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79174.93", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод с карты на карту",
                "from": "Счет 19708645243245678542",
                "to": "Счет 75651667383060281111",
            }
        ]
    )
)

def card_number_generator() -> Generator[str, int]:
    number = int('1')
    for x in range(9999999999999999):
        numbers = str(number).zfill(16)
        yield f'{numbers[0:4]} {numbers[4:8]} {numbers[8:12]} {numbers[12:]}'
        number += 1


card_number = card_number_generator()

print(next(card_number))
print(next(card_number))
print(next(card_number))
print(next(card_number))




