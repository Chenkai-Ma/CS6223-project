# property to violate: The output datetime object's year, month, and day must match the year, month, and day of the input date object.
from hypothesis import given, strategies as st
import datetime

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_1(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by modifying the year
    result = result.replace(year=result.year + 1)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_2(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by modifying the month
    result = result.replace(month=(result.month % 12) + 1)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_3(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by modifying the day
    result = result.replace(day=result.day + 1 if result.day < 28 else 1)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_4(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by setting an arbitrary year
    result = result.replace(year=9999)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_5(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Violate the property by setting an arbitrary month
    result = result.replace(month=13)  # Invalid month
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day