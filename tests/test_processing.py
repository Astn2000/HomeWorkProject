import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(my_list ,list_executed, list_canceled):
    assert filter_by_state(my_list) == list_executed
    assert filter_by_state(my_list, "CANCELED") == list_canceled


def test_filter_by_state_value_error():
    with pytest.raises(ValueError):
        filter_by_state([])


def test_sort_by_date(list_dict, list_dict_reverse_true, list_dict_reverse_false):
    assert sort_by_date(list_dict) == list_dict_reverse_true
    assert sort_by_date(list_dict, False) == list_dict_reverse_false


def test_sort_by_same_date(test_sort_by_same_date):
    assert sort_by_date(test_sort_by_same_date) == test_sort_by_same_date


def test_sort_by_date_value_error():
    with pytest.raises(ValueError):
        sort_by_date([])
