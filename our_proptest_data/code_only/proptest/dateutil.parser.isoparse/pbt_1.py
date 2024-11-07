from hypothesis import given, strategies as st
from datetime import datetime, timedelta
import dateutil.parser

@given(st.text())
def test_output_is_valid_datetime(dt_str):
    try:
        result = dateutil.parser.isoparse(dt_str)
        assert isinstance(result, datetime)
    except ValueError:
        pass  # Expected for invalid inputs

@given(st.text())
def test_output_for_24_hour_case(dt_str):
    if "24:00" in dt_str:
        result = dateutil.parser.isoparse(dt_str.replace("24:00", "00:00"))
        assert result == datetime.combine(result.date() + timedelta(days=1), datetime.min.time())

@given(st.text())
def test_output_matches_input_components(dt_str):
    try:
        result = dateutil.parser.isoparse(dt_str)
        components = dateutil.parser._parse_isodate(dt_str)
        assert (result.year, result.month, result.day, result.hour, result.minute, result.second) == components
    except ValueError:
        pass  # Expected for invalid inputs

@given(st.text())
def test_value_error_for_unknown_components(dt_str):
    invalid_str = dt_str + "XYZ"  # Append unknown component
    try:
        dateutil.parser.isoparse(invalid_str)
        assert False  # Should raise ValueError
    except ValueError:
        pass

@given(st.text())
def test_timezone_information(dt_str):
    if "+00:00" in dt_str or "-00:00" in dt_str:
        result = dateutil.parser.isoparse(dt_str)
        assert result.tzinfo is not None
    else:
        try:
            result = dateutil.parser.isoparse(dt_str)
            assert result.tzinfo is None
        except ValueError:
            pass  # Expected for invalid inputs
# End program