# property to violate: The output for a date representing a Sunday is always 6.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1(date):
    if date.weekday() == 6:  # If the date is a Sunday
        assert date.weekday() == 5  # Incorrectly asserting it is 5 instead of 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_2(date):
    if date.weekday() == 6:  # If the date is a Sunday
        assert date.weekday() == 4  # Incorrectly asserting it is 4 instead of 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_3(date):
    if date.weekday() == 6:  # If the date is a Sunday
        assert date.weekday() == 3  # Incorrectly asserting it is 3 instead of 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_4(date):
    if date.weekday() == 6:  # If the date is a Sunday
        assert date.weekday() == 2  # Incorrectly asserting it is 2 instead of 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_5(date):
    if date.weekday() == 6:  # If the date is a Sunday
        assert date.weekday() == 1  # Incorrectly asserting it is 1 instead of 6