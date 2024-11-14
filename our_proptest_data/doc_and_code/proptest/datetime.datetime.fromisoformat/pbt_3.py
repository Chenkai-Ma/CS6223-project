from hypothesis import given, strategies as st
from datetime import datetime, timedelta
import re

# Define a strategy for generating valid ISO 8601 date strings
def valid_iso_date_strings():
    return st.one_of(
        st.builds(lambda year, month, day: f"{year:04}-{month:02}-{day:02}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31)),
        st.builds(lambda year, month, day, hour, minute, second: 
                   f"{year:04}-{month:02}-{day:02}T{hour:02}:{minute:02}:{second:02}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31),
                   st.integers(min_value=0, max_value=23),
                   st.integers(min_value=0, max_value=59),
                   st.integers(min_value=0, max_value=59)),
        st.builds(lambda year, month, day, hour, minute, second, tz: 
                   f"{year:04}-{month:02}-{day:02}T{hour:02}:{minute:02}:{second:02}{tz}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31),
                   st.integers(min_value=0, max_value=23),
                   st.integers(min_value=0, max_value=59),
                   st.integers(min_value=0, max_value=59),
                   st.one_of(st.just('+00:00'), st.just('-05:00'))),
    )

@given(valid_iso_date_strings())
def test_output_validity_property(date_string):
    dt = datetime.fromisoformat(date_string)
    year, month, day = dt.year, dt.month, dt.day
    assert 1 <= month <= 12
    assert 1 <= day <= 31  # Simplified check; a more complex check could be done

@given(valid_iso_date_strings())
def test_output_time_components_property(date_string):
    dt = datetime.fromisoformat(date_string)
    if 'T' in date_string:
        time_part = date_string.split('T')[1].split('+')[0].split('-')[0]
        time_components = re.findall(r'\d+', time_part)
        assert len(time_components) <= 3  # Only hour, minute, second
        assert all(0 <= int(tc) < 60 for tc in time_components[1:])  # Minute and second checks
        if time_components:
            assert 0 <= int(time_components[0]) < 24  # Hour check

@given(valid_iso_date_strings())
def test_output_timezone_property(date_string):
    dt = datetime.fromisoformat(date_string)
    if 'Z' in date_string or re.search(r'[+-]\d{2}:\d{2}', date_string):
        assert dt.tzinfo is not None
    else:
        assert dt.tzinfo is None

@given(st.text())
def test_invalid_format_property(invalid_date_string):
    try:
        datetime.fromisoformat(invalid_date_string)
        assert False, f"Expected ValueError for invalid date string: {invalid_date_string}"
    except ValueError:
        pass  # Expected exception

@given(valid_iso_date_strings())
def test_default_midnight_property(date_string):
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.fromisoformat(date_string)
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0
# End program