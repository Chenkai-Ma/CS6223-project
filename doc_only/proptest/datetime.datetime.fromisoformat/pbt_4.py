from hypothesis import given, strategies as st
from datetime import datetime, timezone, timedelta
import re

@st.composite
def iso_datetime_strings(draw):
    # Generate valid ISO 8601 date strings
    year = draw(st.integers(min_value=1, max_value=9999))
    month = draw(st.integers(min_value=1, max_value=12))
    day = draw(st.integers(min_value=1, max_value=31))
    hour = draw(st.integers(min_value=0, max_value=23))
    minute = draw(st.integers(min_value=0, max_value=59))
    second = draw(st.integers(min_value=0, max_value=59))
    microsecond = draw(st.integers(min_value=0, max_value=999999))
    
    # Timezone offset
    tz_offset = draw(st.one_of(
        st.just('Z'),  # UTC
        st.timezones()  # Random timezone offsets
    ))
    
    if tz_offset == 'Z':
        return f"{year:04d}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}.{microsecond:06d}Z"
    else:
        return f"{year:04d}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}.{microsecond:06d}{tz_offset}"

@given(iso_datetime_strings())
def test_output_is_valid_datetime_property(date_string):
    # Test that the output is a valid datetime object
    dt = datetime.fromisoformat(date_string)
    assert isinstance(dt, datetime)

@given(iso_datetime_strings())
def test_date_attributes_match_input_property(date_string):
    # Test that the year, month, and day attributes correspond to input
    dt = datetime.fromisoformat(date_string)
    year, month, day = map(int, re.findall(r'\d+', date_string.split('T')[0]))
    assert dt.year == year
    assert dt.month == month
    assert dt.day == day

@given(iso_datetime_strings())
def test_time_attributes_match_input_property(date_string):
    # Test that time attributes match if present
    dt = datetime.fromisoformat(date_string)
    time_part = date_string.split('T')[1] if 'T' in date_string else None
    if time_part:
        time_parts = re.findall(r'\d+', time_part)
        if len(time_parts) >= 3:  # hour, minute, second are present
            hour, minute, second = map(int, time_parts[:3])
            assert dt.hour == hour
            assert dt.minute == minute
            assert dt.second == second
            if len(time_parts) == 4:  # microsecond is present
                microsecond = int(time_parts[3])
                assert dt.microsecond == microsecond

@given(iso_datetime_strings())
def test_timezone_info_property(date_string):
    # Test that tzinfo is set correctly if timezone is present
    dt = datetime.fromisoformat(date_string)
    if 'Z' in date_string or re.search(r'([+-]\d{2}:\d{2})', date_string):
        assert dt.tzinfo is not None
    else:
        assert dt.tzinfo is None

@given(iso_datetime_strings())
def test_default_to_midnight_property(date_string):
    # Test that it defaults to midnight if no time is provided
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.fromisoformat(date_string)
        assert dt.hour == 0
        assert dt.minute == 0
        assert dt.second == 0
        assert dt.microsecond == 0
# End program