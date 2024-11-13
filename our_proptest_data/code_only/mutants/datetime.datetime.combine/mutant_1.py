# property to violate: The output datetime object should have the same year, month, and day as the provided date argument.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_datetime_combine_1(date):
    result = datetime.datetime.combine(date, datetime.time(12, 0)) + datetime.timedelta(days=1)
    assert result.year == date.year and result.month == date.month and result.day == date.day

@given(st.dates())
def test_violation_of_datetime_datetime_combine_2(date):
    result = datetime.datetime.combine(date, datetime.time(12, 0)) + datetime.timedelta(days=-1)
    assert result.year == date.year and result.month == date.month and result.day == date.day

@given(st.dates())
def test_violation_of_datetime_datetime_combine_3(date):
    result = datetime.datetime.combine(date, datetime.time(12, 0), tzinfo=datetime.timezone.utc)
    result = result.replace(year=result.year + 1)  # Increment year to violate property
    assert result.year == date.year and result.month == date.month and result.day == date.day

@given(st.dates())
def test_violation_of_datetime_datetime_combine_4(date):
    result = datetime.datetime.combine(date, datetime.time(12, 0))
    result = result.replace(month=result.month + 1 if result.month < 12 else 1)  # Increment month to violate property
    assert result.year == date.year and result.month == date.month and result.day == date.day

@given(st.dates())
def test_violation_of_datetime_datetime_combine_5(date):
    result = datetime.datetime.combine(date, datetime.time(12, 0))
    result = result.replace(day=result.day + 1 if result.day < 28 else 1)  # Increment day to violate property
    assert result.year == date.year and result.month == date.month and result.day == date.day