from hypothesis import given, strategies as st
from dateutil import parser
from datetime import datetime, timedelta
import re

@given(st.text())
def test_output_represents_input_date_time(dt_str):
    try:
        result = parser.isoparse(dt_str)
        # Extract components from the input string
        match = re.match(r'(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?(?:T(\d{2}):?(\d{2})?:?(\d{2})?(?:\.(\d+))?)?(Z|[+-]\d{2}:?\d{2}|[+-]\d{2}\d{2}|[+-]\d{2})?$', dt_str)
        if match:
            year, month, day, hour, minute, second, _, tz = match.groups()
            # Compare parsed result components
            assert result.year == int(year)
            assert result.month == (int(month) if month else 1)
            assert result.day == (int(day) if day else 1)
            assert result.hour == (int(hour) if hour else 0)
            assert result.minute == (int(minute) if minute else 0)
            assert result.second == (int(second) if second else 0)
    except (ValueError, TypeError):
        pass  # Handle invalid ISO-8601 strings that raise exceptions

@given(st.text())
def test_output_timezone_offset(dt_str):
    try:
        result = parser.isoparse(dt_str)
        if re.search(r'[+-]\d{2}:\d{2}|Z', dt_str):  # Check if there's a timezone
            assert result.tzinfo is not None
            # Check if UTC is correctly represented
            if 'Z' in dt_str or '+00' in dt_str or '-00' in dt_str:
                assert result.tzinfo.utcoffset(result) == timedelta(0)
    except (ValueError, TypeError):
        pass  # Handle invalid ISO-8601 strings that raise exceptions

@given(st.text())
def test_unspecified_components_default(dt_str):
    try:
        result = parser.isoparse(dt_str)
        if re.match(r'^\d{4}(-\d{2}){0,2}T?(\d{2}:\d{2}:\d{2})?$', dt_str):
            assert result.month == (int(re.search(r'-(\d{2})', dt_str).group(1)) if re.search(r'-(\d{2})', dt_str) else 1)
            assert result.day == (int(re.search(r'-(\d{2})$', dt_str).group(1)) if re.search(r'-(\d{2})$', dt_str) else 1)
            assert result.hour == (int(re.search(r'T(\d{2})', dt_str).group(1)) if re.search(r'T(\d{2})', dt_str) else 0)
            assert result.minute == (int(re.search(r'(\d{2}):(\d{2})', dt_str).group(2)) if re.search(r'(\d{2}):(\d{2})', dt_str) else 0)
            assert result.second == (int(re.search(r'(\d{2}):(\d{2}):(\d{2})', dt_str).group(3)) if re.search(r'(\d{2}):(\d{2}):(\d{2})', dt_str) else 0)
    except (ValueError, TypeError):
        pass  # Handle invalid ISO-8601 strings that raise exceptions

@given(st.text())
def test_midnight_special_case(dt_str):
    try:
        result = parser.isoparse(dt_str)
        if '00:00' in dt_str or '24:00' in dt_str:
            assert result.hour == 0
            assert result.minute == 0
    except (ValueError, TypeError):
        pass  # Handle invalid ISO-8601 strings that raise exceptions

@given(st.text())
def test_invalid_strings_raise_error(dt_str):
    if not re.match(r'^\d{4}(-\d{2}){0,2}T?(\d{2}:\d{2}:\d{2})?$', dt_str):
        try:
            parser.isoparse(dt_str)
            assert False  # Should raise an error for invalid strings
        except ValueError:
            assert True  # Expected behavior
        except TypeError:
            assert True  # Expected behavior
# End program