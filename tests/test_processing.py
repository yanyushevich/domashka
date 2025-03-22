import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import function_output_1, function_output_2, function_reverse_, function_reverse_2


def test_filter_by_state(input_data_true, function_output_1, function_output_2):
    assert filter_by_state(input_data_true) == function_output_1
    assert filter_by_state(input_data_true, "CANCELED") == function_output_2


with pytest.raises(TypeError):
    filter_by_state()


def test_sort_by_date(input_data_true, function_reverse_, function_reverse_2):
    assert sort_by_date(input_data_true) == function_reverse_
    assert sort_by_date(input_data_true, sorting_direction=False) == function_reverse_2


assert sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
)
assert sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "201907-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
)
