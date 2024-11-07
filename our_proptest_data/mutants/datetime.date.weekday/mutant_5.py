# property to violate: The output for a date that is one week apart (i.e., adding or subtracting 7 days) remains the same.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1(date):
    one_week_later = date + datetime.timedelta(weeks=1)
    assert date.weekday() != one_week_later.weekday()  # Change to not equal

@given(st.dates())
def test_violation_of_datetime_date_weekday_2(date):
    one_week_later = date + datetime.timedelta(weeks=1)
    assert date.weekday() + 1 == one_week_later.weekday()  # Shift the output by 1

@given(st.dates())
def test_violation_of_datetime_date_weekday_3(date):
    one_week_later = date + datetime.timedelta(weeks=1)
    assert date.weekday() + 2 == one_week_later.weekday()  # Shift the output by 2

@given(st.dates())
def test_violation_of_datetime_date_weekday_4(date):
    one_week_later = date + datetime.timedelta(weeks=1)
    assert date.weekday() + 3 == one_week_later.weekday()  # Shift the output by 3

@given(st.dates())
def test_violation_of_datetime_date_weekday_5(date):
    one_week_later = date + datetime.timedelta(weeks=1)
    assert date.weekday() - 1 == one_week_later.weekday()  # Shift the output by -1