from hypothesis import given, strategies as st
from datetime import datetime, timedelta
import dateutil.parser

@given(st.text())
def test_output_is_valid_datetime_property(dt_str):
    try:
        result = dateutil.parser.isoparse(dt_str)
        assert isinstance(result, datetime)
    except ValueError:
        pass  # Expected if the input string is invalid

@given(st.text())
def test_output_for_24_hour_case_property(dt_str):
    if "24:00" in dt_str:
        result = dateutil.parser.isoparse(dt_str.replace("24:00", "00:00"))
        assert result == datetime(*dateutil.parser._parse_isodate(dt_str)[0]) + timedelta(days=1)

@given(st.text())
def test_output_year_month_day_hour_minute_second_property(dt_str):
    try:
        components, pos = dateutil.parser._parse_isodate(dt_str)
        result = dateutil.parser.isoparse(dt_str)
        assert result.year == components[0]
        assert result.month == components[1]
        assert result.day == components[2]
        assert result.hour == components[3] % 24  # Adjust for 24 hour case
    except ValueError:
        pass  # Expected if the input string is invalid

@given(st.text())
def test_value_error_for_unknown_iso_components_property(dt_str):
    bad_str = dt_str + "XYZ"
    try:
        dateutil.parser.isoparse(bad_str)
        assert False  # We expect a ValueError
    except ValueError:
        assert True  # Expected

@given(st.text())
def test_timezone_information_property(dt_str):
    if any(tz in dt_str for tz in ['Z', '+', '-']):
        result = dateutil.parser.isoparse(dt_str)
        assert result.tzinfo is not None  # Ensure timezone info is present

# End program