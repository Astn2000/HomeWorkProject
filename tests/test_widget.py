import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_or_card_number, type_number, expected",
    [
        ("Visa Gold", "1234567812345678", "Visa Gold 1234 56** **** 5678"),
        ("Счет", "73654108430135874305", "Счет **4305"),
        ("Visa", "1234567812345678", "Visa 1234 56** **** 5678"),
        ("Счет", "73654108430135874306", "Счет **4306"),
    ],
)
def test_mask_account_card(account_or_card_number: str, type_number: str, expected: str) -> None:
    assert mask_account_card(account_or_card_number , type_number) == expected


def test_mask_account_card_type() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Visa", "qwdsadasdwasdwas")


@pytest.mark.parametrize(
    "string_1, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2023-05-11T02:26:18.671407", "11.05.2023")]
)
def test_get_date_success(string_1: str, expected: str) -> None:
    assert get_date(string_1) == expected


def test_get_date_value_error() ->None :
    with pytest.raises(ValueError):
        get_date("2024-03-1102:26:18.671407")


def test_get_date_value_error_1() -> None:
    with pytest.raises(ValueError):
        get_date("")
