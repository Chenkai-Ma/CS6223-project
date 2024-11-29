# property to violate: If the input date corresponds to a Monday, the output of `weekday()` should be 0.
from hypothesis import given, strategies as st
import datetime

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_1(date):
    if date.weekday() == 0:  # If it's Monday
        assert date.weekday() == 1  # Incorrectly asserting it should be 1 instead of 0

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_2(date):
    if date.weekday() == 0:  # If it's Monday
        assert date.weekday() == 2  # Incorrectly asserting it should be 2 instead of 0

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_3(date):
    if date.weekday() == 0:  # If it's Monday
        assert date.weekday() == 3  # Incorrectly asserting it should be 3 instead of 0

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_4(date):
    if date.weekday() == 0:  # If it's Monday
        assert date.weekday() == 4  # Incorrectly asserting it should be 4 instead of 0

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_5(date):
    if date.weekday() == 0:  # If it's Monday
        assert date.weekday() == 5  # Incorrectly asserting it should be 5 instead of 0