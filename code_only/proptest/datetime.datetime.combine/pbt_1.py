from hypothesis import given, strategies as st
import datetime

@st.composite
def date_time_pairs(draw):
    date = draw(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
    time = draw(st.times())
    return date, time

@given(date_time_pairs())
def test_output_year_month_day_property(date_time):
    date, time = date_time
    result = datetime.datetime.combine(date, time)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(date_time_pairs())
def test_output_hour_minute_second_microsecond_property(date_time):
    date, time = date_time
    result = datetime.datetime.combine(date, time)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond

@given(date_time_pairs())
def test_tzinfo_property_when_true(date_time):
    date, time = date_time
    result = datetime.datetime.combine(date, time, tzinfo=True)
    assert result.tzinfo == time.tzinfo

@given(st.one_of(st.dates(), st.integers()), st.times())
def test_type_error_on_invalid_date_property(invalid_date, time):
    try:
        result = datetime.datetime.combine(invalid_date, time)
        assert False, "Expected TypeError not raised"
    except TypeError:
        pass

@given(st.dates(), st.one_of(st.integers(), st.dates()))
def test_type_error_on_invalid_time_property(date, invalid_time):
    try:
        result = datetime.datetime.combine(date, invalid_time)
        assert False, "Expected TypeError not raised"
    except TypeError:
        pass
# End program