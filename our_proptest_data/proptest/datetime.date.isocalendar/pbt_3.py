from hypothesis import given, strategies as st
from datetime import date

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_year_component_property(d):
    iso_year, _, _ = d.isocalendar()
    if d.isocalendar()[1] == 1:  # Check if it's the first week
        assert iso_year == d.year

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_week_component_property(d):
    _, iso_week, _ = d.isocalendar()
    assert 1 <= iso_week <= 53

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_weekday_component_property(d):
    _, _, iso_weekday = d.isocalendar()
    assert 1 <= iso_weekday <= 7

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_year_difference_property(d):
    iso_year, iso_week, iso_weekday = d.isocalendar()
    if iso_week == 1:  # If it's the first week of the ISO year
        assert iso_year == d.year or (d.month == 12 and d.day >= 29)

@given(st.dates(min_value=date(1, 1, 1), max_value=date(9999, 12, 31)))
def test_valid_iso_calendar_date_property(d):
    iso_year, iso_week, iso_weekday = d.isocalendar()
    assert (iso_weekday == 1 and d.isocalendar()[1] == iso_week) or (iso_weekday == 7 and d.isocalendar()[1] == iso_week)
# End program