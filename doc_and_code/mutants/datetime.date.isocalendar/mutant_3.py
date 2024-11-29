# property to violate: The output weekday must be in the range of 1 to 7, representing Monday through Sunday, inclusive.
from hypothesis import given, strategies as st
from datetime import date

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_1(year, month, day):
    try:
        _, _, iso_weekday = date(year, month, day).isocalendar()
        iso_weekday = iso_weekday + 7  # Shift weekday to be out of range (8 to 14)
        assert 1 <= iso_weekday <= 7
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_2(year, month, day):
    try:
        _, _, iso_weekday = date(year, month, day).isocalendar()
        iso_weekday = 0  # Set weekday to 0, which is out of range
        assert 1 <= iso_weekday <= 7
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_3(year, month, day):
    try:
        _, _, iso_weekday = date(year, month, day).isocalendar()
        iso_weekday = -1  # Set weekday to -1, which is out of range
        assert 1 <= iso_weekday <= 7
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_4(year, month, day):
    try:
        _, _, iso_weekday = date(year, month, day).isocalendar()
        iso_weekday = 15  # Set weekday to 15, which is out of range
        assert 1 <= iso_weekday <= 7
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_5(year, month, day):
    try:
        _, _, iso_weekday = date(year, month, day).isocalendar()
        iso_weekday = 10  # Set weekday to 10, which is out of range
        assert 1 <= iso_weekday <= 7
    except ValueError:
        pass  # Ignore invalid dates