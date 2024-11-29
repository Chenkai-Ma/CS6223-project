from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_year_property(d):
    iso_year, _, _ = d.isocalendar()
    if d.isocalendar()[1] == 1:  # Check if it's the first week of the ISO year
        assert iso_year == d.year

@given(st.dates())
def test_week_property(d):
    week = d.isocalendar()[1]
    assert 1 <= week <= 53  # Week must be between 1 and 53

@given(st.dates())
def test_weekday_property(d):
    weekday = d.isocalendar()[2]
    assert 1 <= weekday <= 7  # Weekday must be between 1 (Monday) and 7 (Sunday)

@given(st.dates())
def test_iso_year_difference_property(d):
    iso_year = d.isocalendar()[0]
    if d.month == 12 and d.day >= 29:  # Check last days of December
        assert iso_year == d.year or iso_year == d.year + 1

@given(st.dates())
def test_valid_iso_calendar_property(d):
    iso_year, week, weekday = d.isocalendar()
    assert (1 <= weekday <= 7) and (1 <= week <= 53)  # Valid ISO week and weekday
# End program