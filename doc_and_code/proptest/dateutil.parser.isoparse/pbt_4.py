from hypothesis import given, strategies as st
from dateutil.parser import isoparse
import datetime

@given(st.text())
def test_output_is_valid_datetime_property(dt_str):
    try:
        result = isoparse(dt_str)
        assert isinstance(result, datetime.datetime)
    except ValueError:
        pass  # Expecting some inputs to raise ValueError

@given(st.text())
def test_incomplete_date_defaults_to_midnight_property(dt_str):
    if any(c in dt_str for c in ['T', 'Z', '+', '-']):
        return  # Only test pure date strings
    try:
        result = isoparse(dt_str)
        assert result.time() == datetime.time(0, 0, 0)
    except ValueError:
        pass  # Expecting some inputs to raise ValueError

@given(st.text())
def test_midnight_24_hours_rollover_property(dt_str):
    if "24:00" in dt_str:
        try:
            result = isoparse(dt_str)
            assert result.time() == datetime.time(0, 0, 0)
            assert result.date() != datetime.datetime.strptime(dt_str.split("T")[0], "%Y-%m-%d").date()
        except ValueError:
            pass  # Expecting some inputs to raise ValueError

@given(st.text())
def test_timezone_offset_correctness_property(dt_str):
    try:
        result = isoparse(dt_str)
        if '+' in dt_str or '-' in dt_str or 'Z' in dt_str:
            assert result.tzinfo is not None
    except ValueError:
        pass  # Expecting some inputs to raise ValueError

@given(st.text())
def test_incomplete_date_formats_default_property(dt_str):
    if any(c in dt_str for c in ['T', 'Z', '+', '-']):
        return  # Only test pure date strings
    try:
        result = isoparse(dt_str)
        year_month_day = dt_str.split('-')
        if len(year_month_day) == 2:  # YYYY-MM
            assert result.day == 1
        elif len(year_month_day) == 1:  # YYYY
            assert result.month == 1 and result.day == 1
    except ValueError:
        pass  # Expecting some inputs to raise ValueError
# End program