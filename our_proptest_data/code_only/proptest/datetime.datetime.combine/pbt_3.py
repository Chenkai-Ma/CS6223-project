from hypothesis import given, strategies as st
import datetime

@st.composite
def date_time_pairs(draw):
    # Generate valid date and time instances
    date = draw(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
    time = draw(st.times())
    return date, time

@given(date_time_pairs())
def test_output_has_same_year_month_day(date_time):
    date, time = date_time
    result = datetime.datetime.combine(date, time)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(date_time_pairs())
def test_output_has_same_hour_minute_second_microsecond(date_time):
    date, time = date_time
    result = datetime.datetime.combine(date, time)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond

@given(date_time_pairs())
def test_output_timezone_if_tzinfo_true(date_time):
    date, time = date_time
    result = datetime.datetime.combine(date, time, tzinfo=True)
    assert result.tzinfo == time.tzinfo

@given(st.one_of(
    st.integers(min_value=1, max_value=9999),
    st.floats(min_value=1, max_value=9999),
    st.text()
))
def test_type_error_for_invalid_date(invalid_date):
    invalid_time = datetime.time()
    try:
        datetime.datetime.combine(invalid_date, invalid_time)
        assert False, "Expected TypeError for invalid date"
    except TypeError:
        pass

@given(st.one_of(
    st.integers(min_value=0, max_value=23),
    st.floats(min_value=0, max_value=23),
    st.text()
))
def test_type_error_for_invalid_time(invalid_time):
    valid_date = datetime.date.today()
    try:
        datetime.datetime.combine(valid_date, invalid_time)
        assert False, "Expected TypeError for invalid time"
    except TypeError:
        pass
# End program