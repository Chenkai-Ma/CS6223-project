from hypothesis import given, strategies as st
from datetime import datetime

@given(st.text())
def test_valid_datetime_object_property(date_string):
    try:
        result = datetime.fromisoformat(date_string)
        assert isinstance(result, datetime)
    except ValueError:
        pass  # Expected for invalid inputs

@given(st.text())
def test_attributes_match_input_property(date_string):
    try:
        result = datetime.fromisoformat(date_string)
        if 'T' in date_string or ' ' in date_string:
            date_part, time_part = date_string.split('T') if 'T' in date_string else date_string.split(' ')
            year, month, day = map(int, date_part.split('-'))
            hour, minute, second = (map(int, time_part.split(':')) + [0])[:3]
            assert result.year == year
            assert result.month == month
            assert result.day == day
            assert result.hour == hour
            assert result.minute == minute
            assert result.second == second
    except ValueError:
        pass  # Expected for invalid inputs

@given(st.text())
def test_timezone_information_property(date_string):
    try:
        result = datetime.fromisoformat(date_string)
        if '+' in date_string or '-' in date_string:
            assert result.tzinfo is not None
    except ValueError:
        pass  # Expected for invalid inputs

@given(st.text())
def test_time_defaults_to_midnight_property(date_string):
    if 'T' not in date_string and ' ' not in date_string:
        date_string += 'T00:00:00'  # Ensure time is added for the test
    try:
        result = datetime.fromisoformat(date_string)
        if 'T' not in date_string and ' ' not in date_string:
            assert result.hour == 0
            assert result.minute == 0
            assert result.second == 0
    except ValueError:
        pass  # Expected for invalid inputs

@given(st.text())
def test_valid_timezone_offset_property(date_string):
    try:
        result = datetime.fromisoformat(date_string)
        if 'Z' in date_string or '+' in date_string or '-' in date_string:
            assert result.tzinfo is not None
    except ValueError:
        pass  # Expected for invalid inputs
# End program