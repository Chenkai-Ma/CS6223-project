# property to violate: If the input date argument is a datetime object, the output must retain the date components of that datetime object, disregarding any time components or tzinfo attributes from it.
from hypothesis import given, strategies as st
import datetime

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_1(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violation: Changing the year to a fixed value
    result = result.replace(year=2020)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_2(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violation: Changing the month to a fixed value
    result = result.replace(month=12)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_3(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violation: Changing the day to a fixed value
    result = result.replace(day=15)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_4(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violation: Changing the hour to a fixed value
    result = result.replace(hour=6)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_5(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violation: Changing the minute to a fixed value
    result = result.replace(minute=30)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute