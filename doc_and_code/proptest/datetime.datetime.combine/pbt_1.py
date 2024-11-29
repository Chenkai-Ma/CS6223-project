from hypothesis import given, strategies as st
from datetime import datetime, date, time

@given(st.dates(), st.times(), st.booleans())
def test_year_month_day_property(input_date, input_time, tzinfo):
    result = datetime.combine(input_date, input_time, tzinfo)
    assert result.year == input_date.year
    assert result.month == input_date.month
    assert result.day == input_date.day

@given(st.dates(), st.times(), st.booleans())
def test_hour_minute_second_microsecond_property(input_date, input_time, tzinfo):
    result = datetime.combine(input_date, input_time, tzinfo)
    assert result.hour == input_time.hour
    assert result.minute == input_time.minute
    assert result.second == input_time.second
    assert result.microsecond == input_time.microsecond

@given(st.dates(), st.times(), st.booleans())
def test_tzinfo_property(input_date, input_time, tzinfo):
    result = datetime.combine(input_date, input_time, tzinfo)
    expected_tzinfo = input_time.tzinfo if not tzinfo else tzinfo
    assert result.tzinfo == expected_tzinfo

@given(st.datetimes(), st.booleans())
def test_datetime_argument_property(input_datetime, tzinfo):
    result = datetime.combine(input_datetime.date(), input_datetime.time(), tzinfo)
    assert result == input_datetime.replace(hour=0, minute=0, second=0, microsecond=0)

@given(st.dates(), st.times())
def test_fold_attribute_property(input_date, input_time):
    result = datetime.combine(input_date, input_time)
    assert result.fold == input_time.fold
# End program