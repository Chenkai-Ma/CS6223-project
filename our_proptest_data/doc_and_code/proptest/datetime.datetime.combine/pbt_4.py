from hypothesis import given, strategies as st
from datetime import datetime, date, time, timedelta

@given(st.dates(), st.times(), st.one_of(st.none(), st.times()), st.booleans())
def test_year_month_day_property(date_input, time_input, tzinfo_input, use_tzinfo):
    result = datetime.combine(date_input, time_input, tzinfo=tzinfo_input if use_tzinfo else None)
    assert result.year == date_input.year
    assert result.month == date_input.month
    assert result.day == date_input.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.times()), st.booleans())
def test_hour_minute_second_microsecond_property(date_input, time_input, tzinfo_input, use_tzinfo):
    result = datetime.combine(date_input, time_input, tzinfo=tzinfo_input if use_tzinfo else None)
    assert result.hour == time_input.hour
    assert result.minute == time_input.minute
    assert result.second == time_input.second
    assert result.microsecond == time_input.microsecond

@given(st.dates(), st.times(), st.one_of(st.none(), st.times()), st.booleans())
def test_tzinfo_property(date_input, time_input, tzinfo_input, use_tzinfo):
    result = datetime.combine(date_input, time_input, tzinfo=tzinfo_input if use_tzinfo else None)
    expected_tzinfo = tzinfo_input if use_tzinfo else time_input.tzinfo
    assert result.tzinfo == expected_tzinfo

@given(st.datetimes(), st.one_of(st.none(), st.times()), st.booleans())
def test_datetime_object_property(datetime_input, tzinfo_input, use_tzinfo):
    date_input = datetime_input.date()
    time_input = datetime_input.time()
    result = datetime.combine(date_input, time_input, tzinfo=tzinfo_input if use_tzinfo else None)
    assert result == datetime_input.replace(tzinfo=None)

@given(st.dates(), st.times())
def test_fold_property(date_input, time_input):
    result = datetime.combine(date_input, time_input)
    assert result.fold == time_input.fold

# End program