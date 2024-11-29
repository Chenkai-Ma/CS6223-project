from hypothesis import given, strategies as st
import datetime

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_datetime_date_isocalendar_year_output_property(dt):
    iso_calendar = dt.isocalendar()
    year = iso_calendar[0]
    if dt.month == 1 and dt.day <= 7 and dt.weekday() == 0:  # First week condition
        assert year == dt.year
    else:
        assert year == dt.isocalendar()[0]

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_datetime_date_isocalendar_week_range_property(dt):
    week = dt.isocalendar()[1]
    assert 1 <= week <= 53

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_datetime_date_isocalendar_day_range_property(dt):
    day = dt.isocalendar()[2]
    assert 1 <= day <= 7

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_datetime_date_isocalendar_week_one_property(dt):
    iso_calendar = dt.isocalendar()
    year = iso_calendar[0]
    if iso_calendar[1] == 1:  # First week
        assert year == dt.year or year == dt.year - 1

@given(st.datetimes(min_value=datetime.datetime(1, 1, 1), max_value=datetime.datetime(9999, 12, 31)))
def test_datetime_date_isocalendar_end_of_year_property(dt):
    if dt.month == 12 and dt.day == 31:
        week = dt.isocalendar()[1]
        year = dt.isocalendar()[0]
        if dt >= datetime.datetime(year + 1, 1, 1, 0, 0):  # After new year's day
            assert week == 1 or week == 53
        else:
            assert week == 53
# End program