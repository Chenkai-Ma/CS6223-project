from hypothesis import given, strategies as st
from datetime import datetime, timedelta
import re

# Strategy to generate valid ISO 8601 date strings
@st.composite
def iso_format_dates(draw):
    year = draw(st.integers(min_value=1, max_value=9999))
    month = draw(st.integers(min_value=1, max_value=12))
    day = draw(st.integers(min_value=1, max_value=31))
    hour = draw(st.integers(min_value=0, max_value=23))
    minute = draw(st.integers(min_value=0, max_value=59))
    second = draw(st.integers(min_value=0, max_value=59))
    microsecond = draw(st.integers(min_value=0, max_value=999999))
    tz_offset = draw(st.one_of(st.just('Z'), st.from_regex(r'[\+\-]\d{2}:\d{2}')))
    
    # Generate a valid ISO 8601 string
    date_string = f'{year:04}-{month:02}-{day:02}T{hour:02}:{minute:02}:{second:02}.{microsecond:06}{tz_offset}'
    return date_string

@given(iso_format_dates())
def test_datetime_datetime_fromisoformat_validity_property(date_string):
    dt = datetime.fromisoformat(date_string)
    year, month, day, hour, minute, second, microsecond = dt.timetuple()[:7]
    assert 1 <= month <= 12
    assert 1 <= day <= 31
    assert 0 <= hour < 24
    assert 0 <= minute < 60
    assert 0 <= second < 60
    assert 0 <= microsecond < 1000000

@given(iso_format_dates())
def test_datetime_datetime_fromisoformat_time_component_property(date_string):
    dt = datetime.fromisoformat(date_string)
    time_component_present = re.search(r'T(\d{2}):(\d{2}):(\d{2})', date_string)
    if time_component_present:
        hour, minute, second = map(int, time_component_present.groups())
        assert dt.hour == hour
        assert dt.minute == minute
        assert dt.second == second

@given(iso_format_dates())
def test_datetime_datetime_fromisoformat_timezone_property(date_string):
    dt = datetime.fromisoformat(date_string)
    tz_offset = re.search(r'([+\-]\d{2}:\d{2}|Z)', date_string)
    if tz_offset:
        assert dt.tzinfo is not None

@given(st.text())
def test_datetime_datetime_fromisoformat_invalid_strings_property(invalid_string):
    try:
        datetime.fromisoformat(invalid_string)
    except ValueError:
        pass  # Expected behavior
    except TypeError:
        pass  # Expected behavior for non-string inputs

@given(iso_format_dates())
def test_datetime_datetime_fromisoformat_default_time_midnight_property(date_string):
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.fromisoformat(date_string)
        assert dt.hour == 0
        assert dt.minute == 0
        assert dt.second == 0
        assert dt.microsecond == 0

# End program