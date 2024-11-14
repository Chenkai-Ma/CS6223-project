from hypothesis import given, strategies as st
from datetime import date
import sys

@given(st.integers(min_value=1, max_value=sys.maxsize),
       st.integers(min_value=1, max_value=12),
       st.integers(min_value=1, max_value=31))
def test_year_property(year, month, day):
    iso_year, _, _ = date(year, month, day).isocalendar()
    assert iso_year in {year, year - 1, year + 1}

@given(st.integers(min_value=1, max_value=sys.maxsize),
       st.integers(min_value=1, max_value=12),
       st.integers(min_value=1, max_value=31))
def test_week_property(year, month, day):
    _, iso_week, _ = date(year, month, day).isocalendar()
    assert 1 <= iso_week <= 53

@given(st.integers(min_value=1, max_value=sys.maxsize),
       st.integers(min_value=1, max_value=12),
       st.integers(min_value=1, max_value=31))
def test_weekday_property(year, month, day):
    _, _, iso_weekday = date(year, month, day).isocalendar()
    assert 1 <= iso_weekday <= 7

@given(st.integers(min_value=1, max_value=sys.maxsize),
       st.integers(min_value=1, max_value=12),
       st.integers(min_value=1, max_value=31))
def test_first_of_year_property(year, month, day):
    if month == 1 and day == 1:
        iso_year, iso_week, iso_weekday = date(year, month, day).isocalendar()
        if (date(year, month, day).weekday() >= 3):  # Thursday or later
            assert iso_week == 1
        else:
            assert iso_week == 53 or iso_week == 52  # last week of previous year

@given(st.integers(min_value=1, max_value=sys.maxsize),
       st.integers(min_value=1, max_value=12),
       st.integers(min_value=1, max_value=31))
def test_consistency_property(year, month, day):
    result1 = date(year, month, day).isocalendar()
    result2 = date(year, month, day).isocalendar()
    assert result1 == result2
# End program