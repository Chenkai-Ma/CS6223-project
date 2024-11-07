from hypothesis import given, strategies as st
import datetime

@st.composite
def date_time_strategy(draw):
    year = draw(st.integers(min_value=1, max_value=9999))
    month = draw(st.integers(min_value=1, max_value=12))
    day = draw(st.integers(min_value=1, max_value=31))  # Simplified, does not check for month validity
    hour = draw(st.integers(min_value=0, max_value=23))
    minute = draw(st.integers(min_value=0, max_value=59))
    second = draw(st.integers(min_value=0, max_value=59))
    microsecond = draw(st.integers(min_value=0, max_value=999999))
    
    date = datetime.date(year, month, day)
    time = datetime.time(hour, minute, second, microsecond)
    return date, time

@given(date_time_strategy())
def test_datetime_combine_date_property(inputs):
    date, time = inputs
    result = datetime.datetime.combine(date, time)
    assert result.year == date.year
    assert result.month == date.month
    assert result.day == date.day

@given(date_time_strategy())
def test_datetime_combine_time_property(inputs):
    date, time = inputs
    result = datetime.datetime.combine(date, time)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond

@given(date_time_strategy())
def test_datetime_combine_tzinfo_property(inputs):
    date, time = inputs
    result = datetime.datetime.combine(date, time, tzinfo=True)
    assert result.tzinfo == time.tzinfo

@given(st.one_of(
    st.builds(datetime.date, st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31)),
    st.builds(datetime.datetime, st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
))
def test_datetime_combine_invalid_date_property(invalid_date):
    with pytest.raises(TypeError):
        datetime.datetime.combine(invalid_date, datetime.time())

@given(st.one_of(
    st.builds(datetime.time, st.integers(min_value=0, max_value=23), st.integers(min_value=0, max_value=59), st.integers(min_value=0, max_value=59), st.integers(min_value=0, max_value=999999)),
    st.builds(datetime.datetime, st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
))
def test_datetime_combine_invalid_time_property(invalid_time):
    with pytest.raises(TypeError):
        datetime.datetime.combine(datetime.date.today(), invalid_time)

# End program