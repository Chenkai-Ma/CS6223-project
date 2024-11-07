from hypothesis import given, strategies as st
import datetime

# Generate valid date and time instances
@st.composite
def date_time_strategy(draw):
    year = draw(st.integers(min_value=1, max_value=9999))
    month = draw(st.integers(min_value=1, max_value=12))
    day = draw(st.integers(min_value=1, max_value=31))
    hour = draw(st.integers(min_value=0, max_value=23))
    minute = draw(st.integers(min_value=0, max_value=59))
    second = draw(st.integers(min_value=0, max_value=59))
    microsecond = draw(st.integers(min_value=0, max_value=999999))
    
    # Create date and time objects
    date = datetime.date(year, month, day)
    time = datetime.time(hour, minute, second, microsecond)
    
    return date, time

@given(date_time_strategy())
def test_output_date_property(data):
    date, time = data
    dt = datetime.datetime.combine(date, time)
    assert dt.year == date.year
    assert dt.month == date.month
    assert dt.day == date.day

@given(date_time_strategy())
def test_output_time_property(data):
    date, time = data
    dt = datetime.datetime.combine(date, time)
    assert dt.hour == time.hour
    assert dt.minute == time.minute
    assert dt.second == time.second
    assert dt.microsecond == time.microsecond

@given(date_time_strategy())
def test_tzinfo_property(data):
    date, time = data
    dt = datetime.datetime.combine(date, time, tzinfo=True)
    assert dt.tzinfo == time.tzinfo

@given(st.one_of(
    st.builds(datetime.date, st.integers(min_value=1, max_value=9999), 
               st.integers(min_value=1, max_value=12), 
               st.integers(min_value=1, max_value=31)),
    st.builds(datetime.time, st.integers(min_value=0, max_value=23), 
               st.integers(min_value=0, max_value=59), 
               st.integers(min_value=0, max_value=59), 
               st.integers(min_value=0, max_value=999999))
))
def test_invalid_date_property(invalid_date):
    with pytest.raises(TypeError):
        datetime.datetime.combine(invalid_date, datetime.time(12))

@given(st.one_of(
    st.builds(datetime.date, st.integers(min_value=1, max_value=9999), 
               st.integers(min_value=1, max_value=12), 
               st.integers(min_value=1, max_value=31)),
    st.builds(datetime.time, st.integers(min_value=0, max_value=23), 
               st.integers(min_value=0, max_value=59), 
               st.integers(min_value=0, max_value=59), 
               st.integers(min_value=0, max_value=999999))
))
def test_invalid_time_property(invalid_time):
    with pytest.raises(TypeError):
        datetime.datetime.combine(datetime.date.today(), invalid_time)

# End program