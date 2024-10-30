from hypothesis import given, strategies as st
from datetime import datetime, date, time, timedelta

@given(st.dates(), st.times())
def test_datetime_combine_date_property(input_date, input_time):
    result = datetime.combine(input_date, input_time)
    assert result.year == input_date.year
    assert result.month == input_date.month
    assert result.day == input_date.day

@given(st.dates(), st.times())
def test_datetime_combine_time_property(input_date, input_time):
    result = datetime.combine(input_date, input_time)
    assert result.hour == input_time.hour
    assert result.minute == input_time.minute
    assert result.second == input_time.second
    assert result.microsecond == input_time.microsecond

@given(st.dates(), st.times(tzinfo=st.tzinfo()))
def test_datetime_combine_tzinfo_argument_property(input_date, input_time):
    tzinfo = input_time.tzinfo
    result = datetime.combine(input_date, input_time, tzinfo=tzinfo)
    assert result.tzinfo == tzinfo

@given(st.datetimes(), st.times())
def test_datetime_combine_datetime_argument_property(input_datetime, input_time):
    result = datetime.combine(input_datetime, input_time)
    assert result.year == input_datetime.year
    assert result.month == input_datetime.month
    assert result.day == input_datetime.day

@given(st.dates(), st.times(tzinfo=st.one_of(st.none(), st.tzinfo())))
def test_datetime_combine_timezone_aware_property(input_date, input_time):
    tzinfo = input_time.tzinfo if input_time.tzinfo is not None else None
    result = datetime.combine(input_date, input_time, tzinfo=tzinfo)
    if tzinfo is not None:
        assert result.tzinfo is not None
    else:
        assert result.tzinfo is None
# End program