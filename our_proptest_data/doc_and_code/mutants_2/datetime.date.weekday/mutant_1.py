# property to violate: The output of the `weekday()` function is always an integer between 0 and 6, inclusive.
from hypothesis import given, strategies as st
import datetime

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_1(date):
    result = date.weekday() + 7  # This will always be >= 7
    assert 0 <= result <= 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_2(date):
    result = date.weekday() - 1  # This will always be <= -1
    assert 0 <= result <= 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_3(date):
    result = date.weekday() * 2  # This will be >= 0 but can be >= 12 for some dates
    assert 0 <= result <= 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_4(date):
    result = date.weekday() + 10  # This will always be >= 10
    assert 0 <= result <= 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_5(date):
    result = (date.weekday() % 7) + 6  # This will always be >= 6
    assert 0 <= result <= 6