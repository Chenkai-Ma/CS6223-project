from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_year_component_property(d):
    iso_year, iso_week, iso_weekday = d.isocalendar()
    if iso_week == 1 and d.month == 1 and d.day < 8:
        assert iso_year == d.year
    elif iso_week > 1:
        assert iso_year == d.year or iso_year == d.year + 1

@given(st.dates())
def test_week_component_property(d):
    iso_year, iso_week, iso_weekday = d.isocalendar()
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_weekday_component_property(d):
    iso_year, iso_week, iso_weekday = d.isocalendar()
    assert 1 <= iso_weekday <= 7

@given(st.dates())
def test_year_week_boundary_property(d):
    iso_year, iso_week, iso_weekday = d.isocalendar()
    if d.month == 12 and d.day >= 29:
        assert iso_year == d.year or iso_year == d.year + 1

@given(st.dates())
def test_valid_iso_calendar_date_property(d):
    iso_year, iso_week, iso_weekday = d.isocalendar()
    assert 1 <= iso_week <= 53
    assert 1 <= iso_weekday <= 7
# End program