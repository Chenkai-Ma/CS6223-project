# property to violate: The output year must be equal to the input year or the input year ± 1, depending on the ISO week calculation rules.
from hypothesis import given, strategies as st
from datetime import date

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_1(year, month, day):
    try:
        iso_year, _, _ = date(year, month, day).isocalendar()
        assert iso_year in {year + 2}  # Violation: output year is always 2 more than input year
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_2(year, month, day):
    try:
        iso_year, _, _ = date(year, month, day).isocalendar()
        assert iso_year in {year - 2}  # Violation: output year is always 2 less than input year
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_3(year, month, day):
    try:
        iso_year, _, _ = date(year, month, day).isocalendar()
        assert iso_year in {year + 3}  # Violation: output year is always 3 more than input year
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_4(year, month, day):
    try:
        iso_year, _, _ = date(year, month, day).isocalendar()
        assert iso_year in {year - 3}  # Violation: output year is always 3 less than input year
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_violation_of_datetime_date_isocalendar_5(year, month, day):
    try:
        iso_year, _, _ = date(year, month, day).isocalendar()
        assert iso_year in {9999}  # Violation: output year is always 9999 regardless of input
    except ValueError:
        pass  # Ignore invalid dates