# property to violate: The output datetime object's year, month, and day must match the year, month, and day of the input date object.
from hypothesis import given, strategies as st
import datetime

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_1(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Altering the year to violate the property
    result = result.replace(year=result.year + 1)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_2(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Altering the month to violate the property
    result = result.replace(month=(result.month % 12) + 1)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_3(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Altering the day to violate the property
    result = result.replace(day=result.day + 1 if result.day < 28 else 1)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_4(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Setting the day to a fixed incorrect value to violate the property
    result = result.replace(day=99)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_5(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Setting the year to a fixed incorrect value to violate the property
    result = result.replace(year=2000)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day