from hypothesis import given, strategies as st
from datetime import date
import sys

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_year_component_property(dt):
    iso_year, iso_week, iso_weekday = dt.isocalendar()
    if iso_week == 1 and dt.month == 1 and dt.day <= 7:
        assert iso_year == dt.year
    elif iso_week == 53 and dt.month == 12:
        assert iso_year == dt.year or iso_year == dt.year + 1
    else:
        assert iso_year == dt.year

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_week_component_property(dt):
    iso_year, iso_week, iso_weekday = dt.isocalendar()
    assert 1 <= iso_week <= 53

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_weekday_component_property(dt):
    iso_year, iso_week, iso_weekday = dt.isocalendar()
    assert 1 <= iso_weekday <= 7

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_year_week_compatibility_property(dt):
    iso_year, iso_week, iso_weekday = dt.isocalendar()
    if iso_week == 1 and iso_weekday == 1:
        assert dt >= date(iso_year, 1, 1)
    elif iso_week == 53:
        assert dt <= date(iso_year, 12, 31)

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_valid_iso_calendar_date_property(dt):
    iso_year, iso_week, iso_weekday = dt.isocalendar()
    # Check if the derived week and weekday correspond to a valid date range
    first_day_of_week = dt - timedelta(days=dt.isocalendar()[2] - 1)  # Get Monday of that week
    last_day_of_week = first_day_of_week + timedelta(days=6)  # Get Sunday of that week
    assert first_day_of_week.year == iso_year
    assert last_day_of_week.year == iso_year

# End program