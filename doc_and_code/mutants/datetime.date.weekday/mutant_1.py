# property to violate: The output of the `weekday()` function is always an integer between 0 and 6, inclusive.
from hypothesis import given, strategies as st
import datetime

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_1(date):
    result = date.weekday() + 10  # Violates the property by adding 10
    assert 0 <= result <= 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_2(date):
    result = date.weekday() - 1  # Violates the property by subtracting 1
    assert 0 <= result <= 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_3(date):
    result = date.weekday() + 7  # Violates the property by adding 7
    assert 0 <= result <= 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_4(date):
    result = date.weekday() * 2  # Violates the property by multiplying by 2
    assert 0 <= result <= 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_5(date):
    result = date.weekday() + 100  # Violates the property by adding 100
    assert 0 <= result <= 6