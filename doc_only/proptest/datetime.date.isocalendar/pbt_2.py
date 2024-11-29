from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_year_property(d):
    iso_year, _, _ = d.isocalendar()
    if d.isocalendar()[1] == 1:  # Checking for the first week
        assert iso_year == d.year

@given(st.dates())
def test_week_property(d):
    _, iso_week, _ = d.isocalendar()
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_weekday_property(d):
    _, _, iso_weekday = d.isocalendar()
    assert 1 <= iso_weekday <= 7

@given(st.dates())
def test_year_discrepancy_property(d):
    if d.month == 12 and d.isocalendar()[1] == 1:  # Last week of December
        iso_year, _, _ = d.isocalendar()
        assert iso_year != d.year

@given(st.dates())
def test_valid_iso_calendar_date_property(d):
    iso_year, iso_week, iso_weekday = d.isocalendar()
    assert 1 <= iso_week <= 53
    assert 1 <= iso_weekday <= 7
# End program