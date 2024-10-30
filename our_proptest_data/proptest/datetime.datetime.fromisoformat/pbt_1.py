from hypothesis import given, strategies as st
from datetime import datetime, timezone, timedelta
import re

# Helper function to generate valid ISO 8601 date strings
def valid_iso_datetime():
    return st.one_of(
        st.builds(lambda year, month, day: f"{year}-{month:02d}-{day:02d}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31)),
        st.builds(lambda year, month, day, hour, minute, second: 
                   f"{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31),
                   st.integers(min_value=0, max_value=23),
                   st.integers(min_value=0, max_value=59),
                   st.integers(min_value=0, max_value=59)),
        st.builds(lambda year, month, day, hour, minute, second, microsecond: 
                   f"{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}.{microsecond:06d}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31),
                   st.integers(min_value=0, max_value=23),
                   st.integers(min_value=0, max_value=59),
                   st.integers(min_value=0, max_value=59),
                   st.integers(min_value=0, max_value=999999)),
        st.builds(lambda year, month, day, tz_offset: 
                   f"{year}-{month:02d}-{day:02d}T00:00:00{tz_offset}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31),
                   st.sampled_from(['+00:00', '+01:00', '+02:00', '-01:00', '-02:00']))
    )

@given(valid_iso_datetime())
def test_output_validity_property(date_string):
    """The output datetime object should always represent a valid point in time."""
    try:
        result = datetime.fromisoformat(date_string)
        assert isinstance(result, datetime)
    except ValueError:
        assert True  # If a ValueError is raised, it is expected

@given(valid_iso_datetime())
def test_output_date_attributes_property(date_string):
    """The year, month, and day attributes should match the parsed values from the input string."""
    result = datetime.fromisoformat(date_string)
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_string)
    if match:
        year, month, day = map(int, match.groups())
        assert result.year == year
        assert result.month == month
        assert result.day == day

@given(valid_iso_datetime())
def test_output_time_attributes_property(date_string):
    """The time attributes should match the values specified in the input string if present."""
    result = datetime.fromisoformat(date_string)
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(\.\d+)?', date_string)
    if match:
        hour, minute, second = map(int, match.groups()[3:6])
        assert result.hour == hour
        assert result.minute == minute
        assert result.second == second

@given(valid_iso_datetime())
def test_output_timezone_property(date_string):
    """The output should have the correct tzinfo attribute if the input includes a timezone offset."""
    result = datetime.fromisoformat(date_string)
    tz_match = re.search(r'([+-]\d{2}:\d{2})$', date_string)
    if tz_match:
        assert result.tzinfo is not None

@given(st.integers(min_value=1, max_value=9999))
def test_default_midnight_property(year):
    """The output datetime object should default to midnight (00:00:00) if no time is given."""
    date_string = f"{year}-01-01"
    result = datetime.fromisoformat(date_string)
    assert result.hour == 0
    assert result.minute == 0
    assert result.second == 0

# End program