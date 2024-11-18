# property to violate: The year, month, and day of the output datetime object must match the year, month, and day of the input date object.
from hypothesis import given, strategies as st
import datetime

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_1(date, time):
    combined = datetime.datetime.combine(date, time)
    combined = combined.replace(year=date.year + 1)  # Violate year
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_2(date, time):
    combined = datetime.datetime.combine(date, time)
    combined = combined.replace(month=date.month + 1 if date.month < 12 else 1)  # Violate month
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_3(date, time):
    combined = datetime.datetime.combine(date, time)
    combined = combined.replace(day=date.day + 1)  # Violate day
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_4(date, time):
    combined = datetime.datetime.combine(date, time)
    combined = combined.replace(year=date.year - 1)  # Violate year
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day

@given(date=st.dates(), time=st.times())
def test_violation_of_datetime_datetime_combine_5(date, time):
    combined = datetime.datetime.combine(date, time)
    combined = combined.replace(month=date.month - 1 if date.month > 1 else 12)  # Violate month
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day