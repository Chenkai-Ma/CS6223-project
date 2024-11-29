from hypothesis import given, strategies as st
import datetime

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_date_components_property(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times())
def test_time_components_property(date, time):
    result = datetime.datetime.combine(date, time)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_tzinfo_from_time_property(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    if tzinfo is None:
        assert result.tzinfo == time.tzinfo
    else:
        assert result.tzinfo == tzinfo

@given(st.datetimes(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_datetime_object_ignored_time_property(datetime_obj, time, tzinfo):
    result = datetime.datetime.combine(datetime_obj, time, tzinfo)
    assert result.year == datetime_obj.year
    assert result.month == datetime_obj.month
    assert result.day == datetime_obj.day
    assert result.hour == time.hour
    assert result.minute == time.minute

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_timezone_aware_property(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    if tzinfo is not None:
        assert result.tzinfo is not None
    else:
        assert result.tzinfo is None
# End program