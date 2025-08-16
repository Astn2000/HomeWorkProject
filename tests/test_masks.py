import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [("1234567812345678", "1234 56** **** 5678")])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_type() -> None:
    with pytest.raises(ValueError) as ex:
        get_mask_card_number("asfkajhsf")
        assert str(ex.value) == "Неверный тип данных, укажите номер карты"


def test_get_mask_card_number_no_correct_len() -> None:
    with pytest.raises(ValueError) as ex:
        get_mask_card_number("1")
        assert str(ex.value) == "Неверное количество символов"


def test_get_mask_card_number_length(card_number: str, correct_length: int = 16) -> None:
    card_number_length = len(card_number)
    assert card_number_length == correct_length


def test_get_mask_card_number_void_str(card_number: str) -> None:
    assert get_mask_card_number(card_number) != ""


@pytest.mark.parametrize("account_number, expected", [("73654108430135874305", "**4305")])
def test_get_mask_account_number(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_account_number_type() -> None:
    with pytest.raises(ValueError) as ex:
        get_mask_account("asfkajhsf")
        assert str(ex.value) == "Неверный тип данных, укажите номер счета"


def test_get_mask_account_number_no_correct_length() -> None:
    with pytest.raises(ValueError) as ex:
        get_mask_account("1")
        assert str(ex.value) == "Неверное количество символов"
