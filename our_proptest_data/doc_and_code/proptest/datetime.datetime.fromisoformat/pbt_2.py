from hypothesis import given, strategies as st
from datetime import datetime, timedelta
import re

# Helper function to generate valid ISO 8601 date strings
def valid_isoformat_date_strings():
    return st.one_of(
        st.fixed_dictionaries({
            'year': st.integers(min_value=1900, max_value=2100),
            'month': st.integers(min_value=1, max_value=12),
            'day': st.integers(min_value=1, max_value=31),
            'hour': st.integers(min_value=0, max_value=23),
            'minute': st.integers(min_value=0, max_value=59),
            'second': st.integers(min_value=0, max_value=59),
            'microsecond': st.integers(min_value=0, max_value=999999),
            'tz_offset': st.tuples(st.integers(min_value=-14, max_value=14), st.integers(min_value=0, max_value=59)),
        }).map(lambda d: f"{d['year']}-{d['month']:02d}-{d['day']:02d}T{d['hour']:02d}:{d['minute']:02d}:{d['second']:02d}.{d['microsecond']:06d}{f'+{d['tz_offset'][0]:02d}:{d['tz_offset'][1]:02d}' if d['tz_offset'][0] >= 0 else f'-{abs(d['tz_offset'][0]):02d}:{d['tz_offset'][1]:02d}'}")
    )

@given(date_string=valid_isoformat_date_strings())
def test_output_validity_property(date_string):
    dt = datetime.fromisoformat(date_string)
    assert dt.year >= 1900 and dt.year <= 2100
    assert dt.month >= 1 and dt.month <= 12
    assert 1 <= dt.day <= 31  # Note: this does not check for month-specific validity.

@given(date_string=valid_isoformat_date_strings())
def test_output_time_component_property(date_string):
    dt = datetime.fromisoformat(date_string)
    if 'T' in date_string:
        time_part = date_string.split('T')[1].split('+')[0].split('-')[0]
        time_components = re.findall(r'(\d+)', time_part)
        assert len(time_components) >= 3  # At least hour, minute, second.
        assert dt.hour == int(time_components[0])
        assert dt.minute == int(time_components[1])
        assert dt.second == int(time_components[2])

@given(date_string=valid_isoformat_date_strings())
def test_output_timezone_property(date_string):
    dt = datetime.fromisoformat(date_string)
    if '+' in date_string or '-' in date_string:
        assert dt.tzinfo is not None
    else:
        assert dt.tzinfo is None

@given(date_string=st.text(min_size=1, max_size=50))
def test_invalid_format_raises_value_error_property(date_string):
    try:
        datetime.fromisoformat(date_string)
        assert False  # We expect a ValueError
    except ValueError:
        pass  # Expected behavior

@given(date_string=valid_isoformat_date_strings())
def test_default_time_midnight_property(date_string):
    if 'T' not in date_string:
        date_part = date_string.split('+')[0].split('-')[0]
        dt = datetime.fromisoformat(date_string)
        assert dt.hour == 0
        assert dt.minute == 0
        assert dt.second == 0
# End program