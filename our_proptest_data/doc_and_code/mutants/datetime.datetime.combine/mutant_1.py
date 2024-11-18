# property to violate: The year, month, and day of the output datetime object must match the year, month, and day of the input date object.
from hypothesis import given, strategies as st
import datetime

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_1(date, time):
    combined = datetime.datetime.combine(date, time)
    # Modify year to be incorrect
    combined = combined.replace(year=combined.year + 1)
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_2(date, time):
    combined = datetime.datetime.combine(date, time)
    # Modify month to be incorrect
    combined = combined.replace(month=(combined.month % 12) + 1)
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_3(date, time):
    combined = datetime.datetime.combine(date, time)
    # Modify day to be incorrect
    combined = combined.replace(day=combined.day + 1 if combined.day < 28 else 1)
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_4(date, time):
    combined = datetime.datetime.combine(date, time)
    # Set year to a fixed incorrect value
    combined = combined.replace(year=9999)
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_5(date, time):
    combined = datetime.datetime.combine(date, time)
    # Set month to a fixed incorrect value
    combined = combined.replace(month=13)  # Invalid month
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day