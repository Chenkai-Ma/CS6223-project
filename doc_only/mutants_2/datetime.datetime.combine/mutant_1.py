# property to violate: The output datetime object's year, month, and day must match the year, month, and day of the input date object.
from hypothesis import given, strategies as st
import datetime

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_1(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by adding 1 to the year
    assert result.year == date.year + 1
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_2(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by adding 1 to the month
    assert result.year == date.year
    assert result.month == date.month + 1
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_3(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by adding 1 to the day
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day + 1

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_4(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by setting the year to a fixed wrong value
    assert result.year == 2000
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_5(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by setting the month to a fixed wrong value
    assert result.year == date.year
    assert result.month == 12
    assert result.day == date.day