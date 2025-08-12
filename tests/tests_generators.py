import pytest

from src.generators import filter_by_currency


def test_filter_by_currency(test_transactions, test_filter_by_currency_usd, currency: str = "USD"):
    assert list(filter_by_currency(test_transactions, "USD")) == test_filter_by_currency_usd

