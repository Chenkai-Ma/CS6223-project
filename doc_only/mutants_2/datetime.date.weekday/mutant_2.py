# property to violate: The output for a date representing a Monday is always 0.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1(date):
    if date.weekday() == 0:  # If the date is a Monday
        assert date.weekday() == 1  # Incorrectly asserting that Monday is 1

@given(st.dates())
def test_violation_of_datetime_date_weekday_2(date):
    if date.weekday() == 0:  # If the date is a Monday
        assert date.weekday() == 2  # Incorrectly asserting that Monday is 2

@given(st.dates())
def test_violation_of_datetime_date_weekday_3(date):
    if date.weekday() == 0:  # If the date is a Monday
        assert date.weekday() == -1  # Incorrectly asserting that Monday is -1

@given(st.dates())
def test_violation_of_datetime_date_weekday_4(date):
    if date.weekday() == 0:  # If the date is a Monday
        assert date.weekday() == 3  # Incorrectly asserting that Monday is 3

@given(st.dates())
def test_violation_of_datetime_date_weekday_5(date):
    if date.weekday() == 0:  # If the date is a Monday
        assert date.weekday() == 4  # Incorrectly asserting that Monday is 4