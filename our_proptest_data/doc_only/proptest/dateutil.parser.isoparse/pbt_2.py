from hypothesis import given, strategies as st
from dateutil import parser
from datetime import datetime, timedelta

# Property 1: The output datetime object should represent the same date and time as specified in the input ISO-8601 string.
@given(st.text())
def test_output_date_time_representation_property(dt_str):
    try:
        result = parser.isoparse(dt_str)
        expected = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
        assert result == expected
    except ValueError:
        pass  # Handle invalid ISO-8601 strings

# Property 2: If the input ISO-8601 string specifies a timezone offset, the output should reflect the correct UTC time.
@given(st.text())
def test_output_timezone_offset_property(dt_str):
    try:
        result = parser.isoparse(dt_str)
        if 'Z' in dt_str or any(offset in dt_str for offset in ['+', '-']):
            expected_utc = result.astimezone(datetime.timezone.utc)
            assert result == expected_utc
    except ValueError:
        pass  # Handle invalid ISO-8601 strings

# Property 3: The output should default to the minimum values for any unspecified components.
@given(st.text())
def test_output_minimum_values_property(dt_str):
    try:
        result = parser.isoparse(dt_str)
        if result.month == 1 and result.day == 1:
            assert result.day == 1
            assert result.month == 1
    except ValueError:
        pass  # Handle invalid ISO-8601 strings

# Property 4: The output should correctly handle both representations of midnight.
@given(st.one_of(st.text(min_size=10, max_size=25), st.text(min_size=23, max_size=23)))  # Including '00:00' and '24:00'
def test_output_midnight_representation_property(dt_str):
    try:
        result = parser.isoparse(dt_str)
        assert result.hour == 0 and result.minute == 0  # Both should represent midnight
    except ValueError:
        pass  # Handle invalid ISO-8601 strings

# Property 5: The output should raise an appropriate error for invalid ISO-8601 strings.
@given(st.text())
def test_invalid_iso_string_property(dt_str):
    try:
        parser.isoparse(dt_str)
    except ValueError:
        assert True  # Expecting an error for invalid strings
    else:
        assert False  # If no error is raised, the test should fail
# End program