from hypothesis import given, strategies as st
from datetime import datetime
import re

# A strategy to generate valid ISO format datetime strings
def valid_iso_format_datetime():
    # Generate valid years, months, days, hours, minutes, seconds, and microseconds
    years = st.integers(min_value=1, max_value=9999)
    months = st.integers(min_value=1, max_value=12)
    days = st.integers(min_value=1, max_value=31)  # Note: This doesn't ensure valid days in month
    hours = st.integers(min_value=0, max_value=23)
    minutes = st.integers(min_value=0, max_value=59)
    seconds = st.integers(min_value=0, max_value=59)
    microseconds = st.integers(min_value=0, max_value=999999)

    # Generate valid datetime strings
    return (years.map(lambda y: f"{y}-{months.generate()}"
                     f"-{days.generate()}T{hours.generate()}:"
                     f"{minutes.generate()}:{seconds.generate()}.{microseconds.generate()}") 
                     .map(lambda d: re.sub(r'-(\d{1,2})-(\d{1,2})T', f'-{d.split("-")[1]:02}-{d.split("-")[2]:02}T', d)))

@given(valid_iso_format_datetime())
def test_output_is_instance_of_datetime_property(date_string):
    result = datetime.fromisoformat(date_string)
    assert isinstance(result, datetime)

@given(valid_iso_format_datetime())
def test_output_has_valid_date_components_property(date_string):
    result = datetime.fromisoformat(date_string)
    assert result.year >= 1 and result.year <= 9999
    assert result.month >= 1 and result.month <= 12
    assert result.day >= 1 and result.day <= 31  # This is a simplified check

@given(valid_iso_format_datetime())
def test_output_midnight_for_24_hour_property(date_string):
    if "24:00" in date_string:
        result = datetime.fromisoformat(date_string)
        assert result.hour == 0 and result.minute == 0 and result.second == 0

@given(valid_iso_format_datetime())
def test_output_has_valid_time_components_property(date_string):
    result = datetime.fromisoformat(date_string)
    assert result.hour >= 0 and result.hour <= 23
    assert result.minute >= 0 and result.minute <= 59
    assert result.second >= 0 and result.second <= 59
    assert result.microsecond >= 0 and result.microsecond <= 999999

@given(st.text())
def test_invalid_input_raises_value_error_property(invalid_string):
    try:
        datetime.fromisoformat(invalid_string)
    except ValueError:
        pass  # Expected behavior
    else:
        assert False  # If no exception is raised, the test should fail

# End program