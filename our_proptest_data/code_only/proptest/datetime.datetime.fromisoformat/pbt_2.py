from hypothesis import given, strategies as st
from datetime import datetime, timedelta
import re

# Utility function to generate valid ISO format strings
def valid_isoformat_string():
    # Generate valid dates and times in ISO format
    years = st.integers(min_value=1900, max_value=2100)
    months = st.integers(min_value=1, max_value=12)
    days = st.integers(min_value=1, max_value=31)  # Days will be validated later
    hours = st.integers(min_value=0, max_value=23)
    minutes = st.integers(min_value=0, max_value=59)
    seconds = st.integers(min_value=0, max_value=59)
    microseconds = st.integers(min_value=0, max_value=999999)

    def generate_valid_date(year, month, day):
        try:
            datetime(year, month, day)
            return f"{year:04d}-{month:02d}-{day:02d}"
        except ValueError:
            return None

    def generate_valid_time(hour, minute, second, microsecond):
        return f"{hour:02d}:{minute:02d}:{second:02d}.{microsecond:06d}"

    return (years.flatmap(lambda y: months.flatmap(lambda m: days.flatmap(lambda d: st.one_of(
        st.just(generate_valid_date(y, m, d) + "T" + generate_valid_time(0, 0, 0, 0)),
        st.just(generate_valid_date(y, m, d) + "T" + generate_valid_time(hours.generate(), minutes.generate(), seconds.generate(), microseconds.generate()))))))
    )

@given(valid_isoformat_string())
def test_output_is_datetime_property(date_string):
    result = datetime.fromisoformat(date_string)
    assert isinstance(result, datetime)

@given(valid_isoformat_string())
def test_valid_date_components_property(date_string):
    result = datetime.fromisoformat(date_string)
    assert 1 <= result.month <= 12
    assert 1 <= result.day <= 31  # Further validation can be done for specific months if needed

@given(valid_isoformat_string())
def test_midnight_next_day_property(date_string):
    if "24:00" in date_string:
        result = datetime.fromisoformat(date_string)
        assert result.hour == 0 and result.minute == 0 and result.second == 0
        assert result.date() == (datetime.fromisoformat(date_string.split("T")[0]) + timedelta(days=1)).date()

@given(valid_isoformat_string())
def test_time_component_ranges_property(date_string):
    result = datetime.fromisoformat(date_string)
    assert 0 <= result.hour < 24
    assert 0 <= result.minute < 60
    assert 0 <= result.second < 60
    assert 0 <= result.microsecond < 1000000

@given(st.text())
def test_invalid_isoformat_string_property(invalid_string):
    if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,6})?$', invalid_string) and len(invalid_string) >= 7:
        try:
            datetime.fromisoformat(invalid_string)
            assert False, f"Expected ValueError for invalid string: {invalid_string}"
        except ValueError:
            pass  # Expected behavior
# End program