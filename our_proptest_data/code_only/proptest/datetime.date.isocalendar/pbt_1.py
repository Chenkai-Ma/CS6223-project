from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_year_property(date):
    year, week, day = date.isocalendar()
    if week == 1:
        assert year == date.year or year == date.year - 1

@given(st.dates())
def test_week_range_property(date):
    year, week, day = date.isocalendar()
    assert 1 <= week <= 53

@given(st.dates())
def test_day_range_property(date):
    year, week, day = date.isocalendar()
    assert 1 <= day <= 7

@given(st.dates())
def test_first_week_year_property(date):
    year, week, day = date.isocalendar()
    if week == 1:
        assert year == date.year or (date.month == 1 and date.day <= 7 and year == date.year - 1)

@given(st.dates())
def test_last_day_of_year_property(date):
    if date.month == 12 and date.day == 31:
        year, week, day = date.isocalendar()
        if week == 1:
            assert year == date.year + 1 or week == 53
        else:
            assert week == 52 or week == 53
# End program