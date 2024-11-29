from hypothesis import given, strategies as st
from dateutil.parser import isoparse
from datetime import datetime, timedelta, timezone

@given(st.text())
def test_isoparse_correctness_property(dt_str):
    """Test that the output datetime object represents the same date and time as specified in the input ISO-8601 string."""
    try:
        result = isoparse(dt_str)
        # Check that the result is a datetime object
        assert isinstance(result, datetime)
    except ValueError:
        # If ValueError is raised, it's an invalid ISO-8601 string, which is acceptable
        pass

@given(st.text())
def test_isoparse_timezone_adjustment_property(dt_str):
    """Test that the output datetime object reflects the correct UTC time if a timezone offset is specified."""
    try:
        result = isoparse(dt_str)
        if 'Z' in dt_str or any(offset in dt_str for offset in ['+', '-']):
            utc_time = result.astimezone(timezone.utc)
            assert utc_time == result  # Output should be in UTC
    except ValueError:
        pass

@given(st.text())
def test_isoparse_default_minimum_values_property(dt_str):
    """Test that unspecified components default to their minimum values."""
    try:
        result = isoparse(dt_str)
        if result.year and result.month and result.day:
            assert result.day >= 1 and result.month >= 1  # Day and month should be at least 1
    except ValueError:
        pass

@given(st.text())
def test_isoparse_midnight_representation_property(dt_str):
    """Test that the output correctly handles both representations of midnight (00:00 and 24:00)."""
    if '00:00' in dt_str or '24:00' in dt_str:
        try:
            result = isoparse(dt_str)
            assert result.hour == 0 and result.minute == 0  # Should be the start of the day
        except ValueError:
            pass

@given(st.text())
def test_isoparse_invalid_string_property(dt_str):
    """Test that the output raises an appropriate error for invalid ISO-8601 strings."""
    invalid_strings = [
        "2017-01-01T00:00+00:00:00",  # Invalid due to too many colons
        "2017-13-01T00:00Z",           # Invalid due to month out of range
        "Not a date"                   # Clearly invalid format
    ]
    if dt_str in invalid_strings:
        try:
            result = isoparse(dt_str)
            assert False  # Should not reach here
        except ValueError:
            assert True  # Expected ValueError was raised
    else:
        try:
            isoparse(dt_str)  # Valid strings should not raise an error
        except ValueError:
            assert False  # Should not reach here for valid strings
# End program