from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_weekday_output_range_property(date):
    result = date.weekday()
    assert 0 <= result <= 6

@given(st.dates())
def test_weekday_correct_day_property(date):
    day_of_week = date.weekday()
    assert day_of_week == (date.toordinal() + 6) % 7

@given(st.dates())
def test_weekday_consistency_property(date):
    result1 = date.weekday()
    result2 = date.weekday()
    assert result1 == result2

@given(st.dates())
def test_weekday_predictable_change_property(date):
    next_day = date + datetime.timedelta(days=1)
    assert (date.weekday() + 1) % 7 == next_day.weekday()

@given(st.dates())
def test_weekday_periodicity_property(date):
    one_week_later = date + datetime.timedelta(weeks=1)
    assert date.weekday() == one_week_later.weekday()
# End program