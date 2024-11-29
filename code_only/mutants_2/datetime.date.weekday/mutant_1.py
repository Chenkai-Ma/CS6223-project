# property to violate: The output of the `weekday` function should always be an integer between 0 and 6, inclusive.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1(date):
    result = date.weekday() + 10  # Shift the result to always be >= 10
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_2(date):
    result = date.weekday() - 1  # Shift the result to always be < 0
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_3(date):
    result = date.weekday() * 2  # Multiply the result to always be >= 0 and even
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_4(date):
    result = date.weekday() + 7  # Shift the result to always be >= 7
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_5(date):
    result = date.weekday() + 3.5  # Change the result to a float
    assert 0 <= result <= 6