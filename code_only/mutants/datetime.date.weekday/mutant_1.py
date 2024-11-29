# property to violate: The output of the `weekday` function should always be an integer between 0 and 6, inclusive.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1(date):
    result = date.weekday() + 10  # Shift output to be greater than 6
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_2(date):
    result = date.weekday() - 1  # Shift output to be less than 0
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_3(date):
    result = date.weekday() + 7  # Shift output to be greater than 6
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_4(date):
    result = date.weekday() * 2  # Output could be greater than 6
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_5(date):
    result = date.weekday() - 10  # Output will be negative
    assert 0 <= result <= 6