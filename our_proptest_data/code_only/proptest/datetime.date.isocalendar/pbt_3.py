from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_year_correct_for_first_week_property(date):
    iso_calendar_date = date.isocalendar()
    year, week, day = iso_calendar_date
    if week == 1:
        assert year == date.year or year == date.year - 1

@given(st.dates())
def test_output_week_range_property(date):
    iso_calendar_date = date.isocalendar()
    year, week, day = iso_calendar_date
    assert 1 <= week <= 53

@given(st.dates())
def test_output_day_range_property(date):
    iso_calendar_date = date.isocalendar()
    year, week, day = iso_calendar_date
    assert 1 <= day <= 7

@given(st.dates())
def test_week_one_year_adjustment_property(date):
    iso_calendar_date = date.isocalendar()
    year, week, day = iso_calendar_date
    if week == 1:
        assert year == date.year or year == date.year - 1

@given(st.dates())
def test_last_day_of_year_week_property(date):
    if date.month == 12 and date.day == 31:
        iso_calendar_date = date.isocalendar()
        year, week, day = iso_calendar_date
        assert week == 52 or week == 1  # Last week of the year or first week of the next year
# End program