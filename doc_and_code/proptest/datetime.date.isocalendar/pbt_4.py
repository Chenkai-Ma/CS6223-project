from hypothesis import given, strategies as st
from datetime import date
from datetime import timedelta

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_isocalendar_year_property(year, month, day):
    # Adjust for valid date ranges
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = st.integers(min_value=1, max_value=31).example()
    elif month in [4, 6, 9, 11]:
        day = st.integers(min_value=1, max_value=30).example()
    elif month == 2:
        day = st.integers(min_value=1, max_value=29).example()  # Consider leap years later

    dt = date(year, month, day)
    iso_year, week, weekday = dt.isocalendar()
    assert iso_year in {year, year - 1, year + 1}

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_isocalendar_week_property(year, month, day):
    # Adjust for valid date ranges
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = st.integers(min_value=1, max_value=31).example()
    elif month in [4, 6, 9, 11]:
        day = st.integers(min_value=1, max_value=30).example()
    elif month == 2:
        day = st.integers(min_value=1, max_value=29).example()  # Consider leap years later

    dt = date(year, month, day)
    iso_year, week, weekday = dt.isocalendar()
    assert 1 <= week <= 53

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_isocalendar_weekday_property(year, month, day):
    # Adjust for valid date ranges
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = st.integers(min_value=1, max_value=31).example()
    elif month in [4, 6, 9, 11]:
        day = st.integers(min_value=1, max_value=30).example()
    elif month == 2:
        day = st.integers(min_value=1, max_value=29).example()  # Consider leap years later

    dt = date(year, month, day)
    iso_year, week, weekday = dt.isocalendar()
    assert 1 <= weekday <= 7

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_isocalendar_first_of_year_property(year, month, day):
    # Adjust for valid date ranges
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = st.integers(min_value=1, max_value=31).example()
    elif month in [4, 6, 9, 11]:
        day = st.integers(min_value=1, max_value=30).example()
    elif month == 2:
        day = st.integers(min_value=1, max_value=29).example()  # Consider leap years later
        
    if month == 1 and day == 1:
        dt = date(year, month, day)
        iso_year, week, weekday = dt.isocalendar()
        assert week == (1 if dt.weekday() <= 3 else 52)  # Check if it falls into the first week or the last week of the previous year.

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_isocalendar_consistency_property(year, month, day):
    # Adjust for valid date ranges
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = st.integers(min_value=1, max_value=31).example()
    elif month in [4, 6, 9, 11]:
        day = st.integers(min_value=1, max_value=30).example()
    elif month == 2:
        day = st.integers(min_value=1, max_value=29).example()  # Consider leap years later

    dt = date(year, month, day)
    iso_result1 = dt.isocalendar()
    iso_result2 = dt.isocalendar()
    assert iso_result1 == iso_result2
# End program