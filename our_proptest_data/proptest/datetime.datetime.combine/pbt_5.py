from hypothesis import given, strategies as st
import datetime

@given(st.dates(), st.times())
def test_datetime_combine_date_components_property(date, time):
    result = datetime.datetime.combine(date, time)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(st.dates(), st.times())
def test_datetime_combine_time_components_property(date, time):
    result = datetime.datetime.combine(date, time)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond

@given(st.dates(), st.times(), st.one_of(st.none(), st.timezones()))
def test_datetime_combine_tzinfo_property(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo=tzinfo)
    if tzinfo is None:
        assert result.tzinfo == time.tzinfo
    else:
        assert result.tzinfo == tzinfo

@given(st.datetimes(), st.times())
def test_datetime_combine_datetime_argument_property(dt, time):
    result = datetime.datetime.combine(dt, time)
    assert result.year == dt.year
    assert result.month == dt.month
    assert result.day == dt.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.timezones()))
def test_datetime_combine_timezone_aware_property(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo=tzinfo)
    if tzinfo is not None:
        assert result.tzinfo is not None
    else:
        assert result.tzinfo is None
# End program