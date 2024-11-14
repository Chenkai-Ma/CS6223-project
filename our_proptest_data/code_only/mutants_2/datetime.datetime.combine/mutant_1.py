# property to violate: The output datetime object should have the same year, month, and day as the provided date argument.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_datetime_combine_1(date):
    # Modify the date to have a different year
    result = (date.replace(year=date.year + 1)).weekday()
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_datetime_combine_2(date):
    # Modify the date to have a different month
    result = (date.replace(month=(date.month % 12) + 1)).weekday()
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_datetime_combine_3(date):
    # Modify the date to have a different day
    result = (date.replace(day=(date.day % 28) + 1)).weekday()
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_datetime_combine_4(date):
    # Change the date to a fixed date (e.g., January 1, 2000)
    result = datetime.date(2000, 1, 1).weekday()
    assert 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_datetime_combine_5(date):
    # Create a date with a negative year (invalid)
    result = (date.replace(year=-1)).weekday()
    assert 0 <= result <= 6