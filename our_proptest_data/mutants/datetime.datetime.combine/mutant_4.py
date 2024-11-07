# property to violate: If the input date argument is a datetime object, the output must retain the date components of that datetime object, disregarding any time components or tzinfo attributes from it.
from hypothesis import given, strategies as st
import datetime

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_1(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violate the property by changing the year of the result
    result = result.replace(year=result.year + 1)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_2(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violate the property by changing the month of the result
    result = result.replace(month=(result.month % 12) + 1)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_3(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violate the property by changing the day of the result
    result = result.replace(day=(result.day % 31) + 1)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_4(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violate the property by changing the hour of the result
    result = result.replace(hour=(result.hour + 1) % 24)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_5(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    # Violate the property by changing the minute of the result
    result = result.replace(minute=(result.minute + 1) % 60)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute