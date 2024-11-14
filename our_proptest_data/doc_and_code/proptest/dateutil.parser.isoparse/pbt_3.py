from hypothesis import given, strategies as st
from datetime import datetime, timedelta
import dateutil.parser

@given(st.text())
def test_output_is_valid_datetime_property(dt_str):
    try:
        result = dateutil.parser.isoparse(dt_str)
        assert isinstance(result, datetime)
    except ValueError:
        pass  # Expecting some strings to raise ValueError

@given(st.text())
def test_no_time_portion_defaults_to_midnight_property(dt_str):
    if '-' in dt_str and 'T' not in dt_str:  # Only consider date strings without time
        result = dateutil.parser.isoparse(dt_str)
        assert result.time() == datetime.min.time()  # Should be midnight

@given(st.text())
def test_midnight_24_hour_format_next_day_property(dt_str):
    if '24:00' in dt_str:
        result = dateutil.parser.isoparse(dt_str.replace('24:00', '00:00'))
        assert result.time() == datetime.min.time()
        assert result.date() == (datetime.strptime(dt_str.split('T')[0], '%Y-%m-%d') + timedelta(days=1)).date()

@given(st.text())
def test_correctly_reflects_time_zone_offset_property(dt_str):
    if any(offset in dt_str for offset in ['Z', '+', '-']):
        result = dateutil.parser.isoparse(dt_str)
        assert isinstance(result.tzinfo, datetime.tzinfo)  # Should have a timezone info

@given(st.text())
def test_incomplete_date_formats_defaults_property(dt_str):
    if 'T' not in dt_str:  # Check for incomplete dates
        result = dateutil.parser.isoparse(dt_str)
        assert result.day == 1  # Should default to the first day of the month

# End program