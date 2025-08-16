import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list, filter_by_currency_usd: str, filter_by_currency_rub: str) -> None:
    assert list(filter_by_currency(transactions, "RUB")) == filter_by_currency_rub
    assert list(filter_by_currency(transactions, "USD")) == filter_by_currency_usd


def test_filter_by_currency_no_transactions(transactions: list) -> None:
    assert list(filter_by_currency(transactions, "EUR")) == []


def test_filter_by_currency_void_list(no_transactions: list) -> None:
    assert list(filter_by_currency(no_transactions)) == []


def test_transaction_descriptions(transactions: list, descriptions: list) -> None:
    assert list(transaction_descriptions(transactions)) == descriptions


def test_transaction_descriptions_void(no_transactions: list) -> None:
    assert list(transaction_descriptions(no_transactions)) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (10001, 10003, ["0000 0000 0001 0001", "0000 0000 0001 0002", "0000 0000 0001 0003"]),
        (9999999999999997, 9999999999999999, ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_no_correct_type() -> None:
    with pytest.raises(TypeError) as ex:
        list(card_number_generator("123124", "asdsa"))  # type: ignore
        assert str(ex.value) == "Ошибка типа данных"


def test_card_number_generator_no_correct_value() -> None:
    with pytest.raises(ValueError) as ex:
        list(card_number_generator(999999999999, 1))  # type: ignore
        assert str(ex.value) == "Некорректные данные"
