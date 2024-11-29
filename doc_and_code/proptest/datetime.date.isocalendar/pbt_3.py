from hypothesis import given, strategies as st
from datetime import date
import sys

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_output_year_property(year, month, day):
    try:
        iso_year, _, _ = date(year, month, day).isocalendar()
        assert iso_year in {year, year - 1, year + 1}
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_output_week_property(year, month, day):
    try:
        _, iso_week, _ = date(year, month, day).isocalendar()
        assert 1 <= iso_week <= 53
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_output_weekday_property(year, month, day):
    try:
        _, _, iso_weekday = date(year, month, day).isocalendar()
        assert 1 <= iso_weekday <= 7
    except ValueError:
        pass  # Ignore invalid dates

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_first_day_of_year_property(year, month, day):
    if month == 1 and day == 1:
        iso_year, iso_week, iso_weekday = date(year, month, day).isocalendar()
        if iso_weekday >= 4:  # Thursday or later
            assert iso_week == 1
        else:
            assert iso_week == 53  # This part may depend on the year
    
@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_consistent_output_property(year, month, day):
    try:
        iso_calendar_output = date(year, month, day).isocalendar()
        assert iso_calendar_output == date(year, month, day).isocalendar()  # Should be consistent
    except ValueError:
        pass  # Ignore invalid dates
# End program