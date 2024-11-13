# property to violate: The output should exhibit periodicity, such that the `weekday` function returns the same value for dates that are exactly one week apart.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1(date):
    result_today = date.weekday()
    one_week_later = date + datetime.timedelta(weeks=1)
    result_one_week_later = (result_today + 1) % 7  # Change the output to be different
    assert result_today == result_one_week_later

@given(st.dates())
def test_violation_of_datetime_date_weekday_2(date):
    result_today = date.weekday()
    one_week_later = date + datetime.timedelta(weeks=1)
    result_one_week_later = (result_today + 2) % 7  # Change the output to be different
    assert result_today == result_one_week_later

@given(st.dates())
def test_violation_of_datetime_date_weekday_3(date):
    result_today = date.weekday()
    one_week_later = date + datetime.timedelta(weeks=1)
    result_one_week_later = (result_today + 3) % 7  # Change the output to be different
    assert result_today == result_one_week_later

@given(st.dates())
def test_violation_of_datetime_date_weekday_4(date):
    result_today = date.weekday()
    one_week_later = date + datetime.timedelta(weeks=1)
    result_one_week_later = (result_today + 4) % 7  # Change the output to be different
    assert result_today == result_one_week_later

@given(st.dates())
def test_violation_of_datetime_date_weekday_5(date):
    result_today = date.weekday()
    one_week_later = date + datetime.timedelta(weeks=1)
    result_one_week_later = (result_today + 5) % 7  # Change the output to be different
    assert result_today == result_one_week_later