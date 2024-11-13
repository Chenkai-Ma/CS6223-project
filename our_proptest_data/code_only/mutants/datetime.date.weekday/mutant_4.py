# property to violate: The output should change predictably when the input date changes, specifically advancing by 1 for each day increment in the input.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1(date):
    result_today = date.weekday()
    tomorrow = date + datetime.timedelta(days=1)
    result_tomorrow = (result_today + 2) % 7  # Violating the property by adding 2 instead of 1
    assert result_tomorrow == (result_today + 1) % 7

@given(st.dates())
def test_violation_of_datetime_date_weekday_2(date):
    result_today = date.weekday()
    tomorrow = date + datetime.timedelta(days=1)
    result_tomorrow = (result_today + 3) % 7  # Violating the property by adding 3 instead of 1
    assert result_tomorrow == (result_today + 1) % 7

@given(st.dates())
def test_violation_of_datetime_date_weekday_3(date):
    result_today = date.weekday()
    tomorrow = date + datetime.timedelta(days=1)
    result_tomorrow = (result_today + 7) % 7  # Violating the property by adding 7, which doesn't change the day
    assert result_tomorrow == (result_today + 1) % 7

@given(st.dates())
def test_violation_of_datetime_date_weekday_4(date):
    result_today = date.weekday()
    tomorrow = date + datetime.timedelta(days=1)
    result_tomorrow = (result_today - 1) % 7  # Violating the property by subtracting 1 instead of adding
    assert result_tomorrow == (result_today + 1) % 7

@given(st.dates())
def test_violation_of_datetime_date_weekday_5(date):
    result_today = date.weekday()
    tomorrow = date + datetime.timedelta(days=1)
    result_tomorrow = (result_today + 5) % 7  # Violating the property by adding 5 instead of 1
    assert result_tomorrow == (result_today + 1) % 7