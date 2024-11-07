from hypothesis import given, strategies as st
from datetime import datetime, timedelta, timezone
import re

# Generate valid ISO 8601 date strings
def valid_iso_8601():
    return st.one_of(
        st.builds(lambda y, m, d: f"{y:04d}-{m:02d}-{d:02d}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31)),
        st.builds(lambda y, m, d, h, mi, s, ms: f"{y:04d}-{m:02d}-{d:02d}T{h:02d}:{mi:02d}:{s:02d}.{ms:06d}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31),
                   st.integers(min_value=0, max_value=23),
                   st.integers(min_value=0, max_value=59),
                   st.integers(min_value=0, max_value=59),
                   st.integers(min_value=0, max_value=999999)),
        st.builds(lambda y, m, d, tz: f"{y:04d}-{m:02d}-{d:02d}Z",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31)),
        st.builds(lambda y, m, d, h, mi, s, ms, offset: f"{y:04d}-{m:02d}-{d:02d}T{h:02d}:{mi:02d}:{s:02d}.{ms:06d}{offset}",
                   st.integers(min_value=1, max_value=9999),
                   st.integers(min_value=1, max_value=12),
                   st.integers(min_value=1, max_value=31),
                   st.integers(min_value=0, max_value=23),
                   st.integers(min_value=0, max_value=59),
                   st.integers(min_value=0, max_value=59),
                   st.integers(min_value=0, max_value=999999),
                   st.regex(r'([+-]\d{2}:\d{2}|Z)'))
    )

@given(valid_iso_8601())
def test_datetime_fromisoformat_validity_property(date_string):
    # The output should always be a valid datetime object
    result = datetime.fromisoformat(date_string)
    assert isinstance(result, datetime)

@given(valid_iso_8601())
def test_datetime_fromisoformat_date_attributes_property(date_string):
    # Extract year, month, and day from input
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_string)
    if match:
        year, month, day = map(int, match.groups())
        result = datetime.fromisoformat(date_string)
        assert result.year == year
        assert result.month == month
        assert result.day == day

@given(valid_iso_8601())
def test_datetime_fromisoformat_time_attributes_property(date_string):
    # Extract time attributes if they exist
    match = re.match(r'.*T(\d{2}):(\d{2}):(\d{2})(\.\d{1,6})?$', date_string)
    if match:
        hour, minute, second = map(int, match.groups()[:3])
        result = datetime.fromisoformat(date_string)
        assert result.hour == hour
        assert result.minute == minute
        assert result.second == second

@given(valid_iso_8601())
def test_datetime_fromisoformat_timezone_property(date_string):
    # Extract timezone information if it exists
    if 'Z' in date_string or re.search(r'[+-]\d{2}:\d{2}', date_string):
        result = datetime.fromisoformat(date_string)
        assert result.tzinfo is not None
    else:
        result = datetime.fromisoformat(date_string)
        assert result.tzinfo is None

@given(valid_iso_8601())
def test_datetime_fromisoformat_default_midnight_property(date_string):
    # Check if the time defaults to midnight if not specified
    if 'T' not in date_string:
        result = datetime.fromisoformat(date_string)
        assert result.hour == 0
        assert result.minute == 0
        assert result.second == 0
# End program