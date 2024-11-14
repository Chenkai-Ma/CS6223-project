from hypothesis import given, strategies as st
from datetime import datetime, timedelta
import re

# Define a strategy for generating valid ISO 8601 date strings
def valid_iso_date_strings():
    # Examples of valid formats
    formats = [
        'YYYY-MM-DD',
        'YYYYMMDD',
        'YYYY-MM-DDTHH:MM:SS',
        'YYYYMMDDTHHMMSS',
        'YYYY-Www-DdTHH:MM:SS',
        'YYYY-MM-DD HH:MM:SS',
        'YYYY-MM-DDTHH:MM:SSZ',
        'YYYY-MM-DDTHH:MM:SS±HH:MM'
    ]
    
    # Generate strings for valid year, month, day, etc.
    for year in range(2000, 2100):
        for month in range(1, 13):
            for day in range(1, 32):  # Days will be validated later
                if day <= (days_in_month := (31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month != 2 else 29 if year % 4 == 0 else 28)):
                    yield f"{year:04}-{month:02}-{day:02}"
                    yield f"{year}{month:02}{day:02}"
                    yield f"{year:04}-{month:02}-{day:02}T00:00:00"
                    yield f"{year}{month:02}{day:02}T000000"
                    yield f"{year:04}-W01-1T00:00:00"  # Example of week date
                    yield f"{year:04}-{month:02}-{day:02} 00:00:00"
                    yield f"{year:04}-{month:02}-{day:02}T00:00:00Z"
                    yield f"{year:04}-{month:02}-{day:02}T00:00:00+00:00"

@given(st.data())
def test_output_validity_property(data):
    date_string = data.draw(st.sampled_from(list(valid_iso_date_strings())))
    try:
        result = datetime.fromisoformat(date_string)
        # Check if the output is a valid datetime object
        assert isinstance(result, datetime)
        # Validate year, month, and day
        assert result.year == int(date_string[:4])
        assert result.month == int(date_string[5:7])
        assert result.day == int(date_string[8:10])
    except ValueError:
        # Ensure that ValueError is raised for invalid inputs
        pass

@given(st.data())
def test_time_component_property(data):
    date_string = data.draw(st.sampled_from(list(valid_iso_date_strings())))
    time_string = 'T00:00:00'
    if 'T' not in date_string:
        date_string += time_string
    try:
        result = datetime.fromisoformat(date_string)
        # Check if time components are valid
        assert result.hour == 0
        assert result.minute == 0
        assert result.second == 0
        assert result.microsecond == 0
    except ValueError:
        pass

@given(st.data())
def test_timezone_handling_property(data):
    date_string = data.draw(st.sampled_from(list(valid_iso_date_strings())))
    timezone_string = '+00:00'
    if 'Z' not in date_string and not re.search(r'[+-]\d{2}:\d{2}', date_string):
        date_string += timezone_string
    try:
        result = datetime.fromisoformat(date_string)
        # Check if timezone info is correctly set
        if '+' in date_string or '-' in date_string or 'Z' in date_string:
            assert result.tzinfo is not None
    except ValueError:
        pass

@given(st.data())
def test_invalid_input_property(data):
    invalid_date_strings = [
        'invalid-date',
        '2021-13-01',
        '2021-01-32',
        '2021-01-01T25:00:00',
        '2021-01-01T00:60:00',
        '2021-01-01T00:00:60',
        '2021-01-01 25:00:00',
    ]
    date_string = data.draw(st.sampled_from(invalid_date_strings))
    try:
        datetime.fromisoformat(date_string)
        assert False, f"ValueError expected but not raised for {date_string}"
    except ValueError:
        pass

@given(st.data())
def test_default_midnight_time_property(data):
    date_string = data.draw(st.sampled_from(list(valid_iso_date_strings())))
    if 'T' not in date_string:
        date_string += 'T00:00:00'  # Append midnight if no time component
    result = datetime.fromisoformat(date_string)
    # Check if the default time component is midnight
    assert result.hour == 0
    assert result.minute == 0
    assert result.second == 0
    assert result.microsecond == 0

# End program