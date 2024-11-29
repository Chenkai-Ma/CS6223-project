from hypothesis import given, strategies as st
from datetime import datetime, date, time, timedelta

@given(st.dates(), st.times())
def test_datetime_year_month_day_property(date_arg, time_arg):
    dt = datetime.combine(date_arg, time_arg)
    assert dt.year == date_arg.year
    assert dt.month == date_arg.month
    assert dt.day == date_arg.day
# End program

@given(st.dates(), st.times())
def test_datetime_hour_minute_second_microsecond_property(date_arg, time_arg):
    dt = datetime.combine(date_arg, time_arg)
    assert dt.hour == time_arg.hour
    assert dt.minute == time_arg.minute
    assert dt.second == time_arg.second
    assert dt.microsecond == time_arg.microsecond
# End program

@given(st.dates(), st.times())
def test_datetime_tzinfo_true_property(date_arg, time_arg):
    dt = datetime.combine(date_arg, time_arg, tzinfo=True)
    assert dt.tzinfo == time_arg.tzinfo
# End program

@given(st.dates(), st.times())
def test_datetime_type_error_on_invalid_date_property(invalid_date, time_arg):
    invalid_date = 'not_a_date'  # This simulates an invalid date
    try:
        datetime.combine(invalid_date, time_arg)
    except TypeError:
        pass  # Expected exception
    else:
        assert False, "Expected TypeError not raised"
# End program

@given(st.dates(), st.times())
def test_datetime_type_error_on_invalid_time_property(date_arg, invalid_time):
    invalid_time = 'not_a_time'  # This simulates an invalid time
    try:
        datetime.combine(date_arg, invalid_time)
    except TypeError:
        pass  # Expected exception
    else:
        assert False, "Expected TypeError not raised"
# End program