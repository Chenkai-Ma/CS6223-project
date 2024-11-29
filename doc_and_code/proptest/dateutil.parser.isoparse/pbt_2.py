from hypothesis import given, strategies as st
from datetime import datetime, timedelta
from dateutil.parser import isoparse
import pytz

@given(st.text())
def test_output_is_valid_datetime_property(dt_str):
    try:
        result = isoparse(dt_str)
        assert isinstance(result, datetime)
    except ValueError:
        pass  # Expecting ValueError for invalid inputs

@given(st.text())
def test_default_time_to_midnight_property(dt_str):
    if "T" not in dt_str and any(part in dt_str for part in ["-", "Z", "+", ":"]):
        result = isoparse(dt_str)
        assert result.time() == datetime.min.time()  # Should be midnight

@given(st.text())
def test_midnight_as_24_hours_property(dt_str):
    if "24:00" in dt_str:
        result = isoparse(dt_str)
        assert result.time() == datetime.min.time() and result.date() > datetime.now().date()

@given(st.text())
def test_correct_time_zone_offset_property(dt_str):
    if any(offset in dt_str for offset in ["Z", "+", "-"]):
        result = isoparse(dt_str)
        assert result.tzinfo is not None  # Should have a timezone info

@given(st.text())
def test_incomplete_date_format_defaults_property(dt_str):
    if any(part in dt_str for part in ["YYYY-", "YYYY", "YYYY-MM"]):
        result = isoparse(dt_str)
        assert result.day == 1  # Default day should be 1 for incomplete dates

# End program