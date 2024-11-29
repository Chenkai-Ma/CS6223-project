# property to violate: If the input string represents a date without a time portion, the time components of the output `datetime` object default to midnight (00:00:00).
from hypothesis import given, strategies as st
from dateutil.parser import isoparse
from datetime import datetime

@given(st.text())
def test_violation_of_dateutil_parser_isoparse_1(dt_str):
    if "T" not in dt_str and any(char.isdigit() for char in dt_str):
        try:
            result = isoparse(dt_str)
            assert result.time() != datetime.min.time()  # Should not default to midnight
        except ValueError:
            pass  # It's acceptable for the input to raise a ValueError

@given(st.text())
def test_violation_of_dateutil_parser_isoparse_2(dt_str):
    if "T" not in dt_str and any(char.isdigit() for char in dt_str):
        try:
            result = isoparse(dt_str)
            assert result.time() == datetime(2021, 1, 1, 12, 0, 0).time()  # Should not default to midnight
        except ValueError:
            pass  # It's acceptable for the input to raise a ValueError

@given(st.text())
def test_violation_of_dateutil_parser_isoparse_3(dt_str):
    if "T" not in dt_str and any(char.isdigit() for char in dt_str):
        try:
            result = isoparse(dt_str)
            assert result.time() == datetime(2021, 1, 1, 23, 59, 59).time()  # Should not default to midnight
        except ValueError:
            pass  # It's acceptable for the input to raise a ValueError

@given(st.text())
def test_violation_of_dateutil_parser_isoparse_4(dt_str):
    if "T" not in dt_str and any(char.isdigit() for char in dt_str):
        try:
            result = isoparse(dt_str)
            assert result.time() == datetime(2021, 1, 1, 6, 30, 0).time()  # Should not default to midnight
        except ValueError:
            pass  # It's acceptable for the input to raise a ValueError

@given(st.text())
def test_violation_of_dateutil_parser_isoparse_5(dt_str):
    if "T" not in dt_str and any(char.isdigit() for char in dt_str):
        try:
            result = isoparse(dt_str)
            assert result.time() == datetime(2021, 1, 1, 18, 0, 0).time()  # Should not default to midnight
        except ValueError:
            pass  # It's acceptable for the input to raise a ValueError