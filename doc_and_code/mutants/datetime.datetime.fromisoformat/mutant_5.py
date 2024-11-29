# property to violate: The output datetime object should have a default time component of midnight (00:00:00) if the input date string does not include a time component.
from hypothesis import given, strategies as st
from datetime import datetime

@given(valid_iso_date_strings())
def test_violation_of_datetime_datetime_fromisoformat_1(date_string):
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.fromisoformat(date_string)
        # Modify the output to have a non-midnight time component
        dt = dt.replace(hour=1, minute=30, second=0)
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0

@given(valid_iso_date_strings())
def test_violation_of_datetime_datetime_fromisoformat_2(date_string):
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.fromisoformat(date_string)
        # Modify the output to have a non-midnight time component
        dt = dt.replace(hour=12, minute=15, second=30)
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0

@given(valid_iso_date_strings())
def test_violation_of_datetime_datetime_fromisoformat_3(date_string):
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.fromisoformat(date_string)
        # Modify the output to have a non-midnight time component
        dt = dt.replace(hour=23, minute=59, second=59)
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0

@given(valid_iso_date_strings())
def test_violation_of_datetime_datetime_fromisoformat_4(date_string):
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.fromisoformat(date_string)
        # Modify the output to have a non-midnight time component
        dt = dt.replace(hour=6, minute=45, second=0)
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0

@given(valid_iso_date_strings())
def test_violation_of_datetime_datetime_fromisoformat_5(date_string):
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.fromisoformat(date_string)
        # Modify the output to have a non-midnight time component
        dt = dt.replace(hour=18, minute=30, second=30)
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0