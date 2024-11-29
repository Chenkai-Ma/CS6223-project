from hypothesis import given, strategies as st
import datetime

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_output_year_property(dt):
    iso_calendar = dt.isocalendar()
    year = iso_calendar[0]
    week = iso_calendar[1]
    
    if week == 1:
        assert year == dt.year or year == dt.year - 1
    else:
        assert year == dt.year

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_output_week_property(dt):
    iso_calendar = dt.isocalendar()
    week = iso_calendar[1]
    assert 1 <= week <= 53

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_output_day_property(dt):
    iso_calendar = dt.isocalendar()
    day = iso_calendar[2]
    assert 1 <= day <= 7

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_week_one_year_property(dt):
    iso_calendar = dt.isocalendar()
    year = iso_calendar[0]
    week = iso_calendar[1]
    
    if week == 1:
        assert year == dt.year or year == dt.year - 1

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_last_day_of_year_property(dt):
    if dt.month == 12 and dt.day == 31:
        iso_calendar = dt.isocalendar()
        week = iso_calendar[1]
        assert week == 53 or week == 1
# End program