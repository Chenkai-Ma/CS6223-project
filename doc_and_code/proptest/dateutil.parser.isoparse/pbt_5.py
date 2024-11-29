from hypothesis import given, strategies as st
from datetime import datetime, timedelta
import dateutil.parser

@given(st.text())
def test_output_is_valid_datetime_property(dt_str):
    try:
        result = dateutil.parser.isoparse(dt_str)
        assert isinstance(result, datetime)
    except ValueError:
        pass  # Catch invalid ISO strings, as they are expected to raise errors.

@given(st.text())
def test_date_without_time_defaults_to_midnight_property(dt_str):
    if 'T' not in dt_str:
        result = dateutil.parser.isoparse(dt_str)
        assert result.time() == datetime.min.time()  # Should default to midnight (00:00:00).

@given(st.text())
def test_midnight_string_translates_to_next_day_property(dt_str):
    if dt_str == "24:00":
        result = dateutil.parser.isoparse("2023-01-01T24:00")
        assert result == datetime(2023, 1, 2, 0, 0)  # Should return the next day at midnight.

@given(st.text())
def test_time_zone_offset_is_correctly_applied_property(dt_str):
    if 'Z' in dt_str or '+' in dt_str or '-' in dt_str:
        result = dateutil.parser.isoparse(dt_str)
        assert result.tzinfo is not None  # Should have a timezone info if input specified.

@given(st.text())
def test_incomplete_date_formats_return_earliest_valid_date_property(dt_str):
    if len(dt_str) in [7, 4]:  # Formats like YYYY-MM or YYYY
        result = dateutil.parser.isoparse(dt_str)
        assert result.day == 1  # Should default to the first of the month or first day of the year.
# End program