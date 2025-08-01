import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('card_number, expected',
                         [('1234567812345678', '1234 56** **** 5678')])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_type():
    with pytest.raises(ValueError):
        get_mask_card_number('qwdsadasdwasdwas')


def test_get_mask_card_number_length(card_number, correct_length = 16):
    card_number_length = len(card_number)
    assert card_number_length == correct_length


def test_get_mask_card_number_void_str(card_number):
    assert get_mask_card_number(card_number) != ''


@pytest.mark.parametrize('account_number, expected',
                         [('73654108430135874305', '**4305')])
def test_get_mask_account_number(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_number_type():
    with pytest.raises(ValueError):
        get_mask_account('qwdsadasdwasdwas')


def test_get_mask_account_length(account_number, correct_length = 20):
    account_length = len(account_number)
    assert account_length == correct_length
