from typing import Any, Generator, Iterator


def filter_by_currency(transactions_list: list, currency: str = "USD") -> Iterator:
    """Функция обрабатывающая список транзакций выводит транзакции с указанной валютой"""
    return filter(
        lambda x: x.get("operationAmount", {}).get("currency", {}).get("name", "") == currency, transactions_list
    )


def transaction_descriptions(transactions_list: list) -> Generator[Any, Any, None]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции"""
    for transaction in transactions_list:
        description_name = transaction.get("description")
        yield description_name


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Generator[str, None, None]:
    """Функция генератор которая выдает номера банковских карт в формате цифра номера карты"""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Ошибка типа данных")
    if start < 1 or stop > 9999999999999999 or stop < start:
        raise ValueError("Некорректные данные")
    for x in range(start, stop + 1):
        numbers = str(start).zfill(16)
        yield f"{numbers[0:4]} {numbers[4:8]} {numbers[8:12]} {numbers[12:]}"
        start += 1


# if __name__ == "__main__":
#
#     transactions = [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702",
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188",
#         },
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2019-01-20T02:08:58.425572",
#             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702",
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2017-04-04T23:20:05.206878",
#             "operationAmount": {"amount": "79174.93", "currency": {"name": "RUB", "code": "RUB"}},
#             "description": "Перевод с карты на карту",
#             "from": "Счет 19708645243245678542",
#             "to": "Счет 75651667383060281111",
#         },
#     ]
#
#     for _ in filter_by_currency(transactions):
#         print(_)
#     # print(list(transaction_descriptions(transactions)))
#
#     print()
#
#     for description in transaction_descriptions(transactions):
#         print(description)
#
#     print()
#
#     for card in card_number_generator(1, 5):
#         print(card)
