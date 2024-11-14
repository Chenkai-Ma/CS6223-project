from hypothesis import given, strategies as st
from datetime import date
import sys

@given(st.integers(min_value=1, max_value=sys.maxsize), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_output_year_property(year, month, day):
    try:
        result = date(year, month, day).isocalendar()
        assert result.year in {year, year - 1, year + 1}
    except ValueError:
        pass  # Skip invalid date combinations

@given(st.integers(min_value=1, max_value=sys.maxsize), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_output_week_property(year, month, day):
    try:
        result = date(year, month, day).isocalendar()
        assert 1 <= result.week <= 53
    except ValueError:
        pass  # Skip invalid date combinations

@given(st.integers(min_value=1, max_value=sys.maxsize), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_output_weekday_property(year, month, day):
    try:
        result = date(year, month, day).isocalendar()
        assert 1 <= result.weekday <= 7
    except ValueError:
        pass  # Skip invalid date combinations

@given(st.integers(min_value=1, max_value=sys.maxsize), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_first_day_of_year_property(year, month, day):
    if month == 1 and day == 1:  # Check only January 1st
        result = date(year, month, day).isocalendar()
        assert result.week == (1 if (date(year, month, day).weekday() >= 3) else 53)

@given(st.integers(min_value=1, max_value=sys.maxsize), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_consistency_property(year, month, day):
    try:
        result1 = date(year, month, day).isocalendar()
        result2 = date(year, month, day).isocalendar()
        assert result1 == result2
    except ValueError:
        pass  # Skip invalid date combinations
# End program