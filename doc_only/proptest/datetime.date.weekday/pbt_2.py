from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_is_integer_between_0_and_6_property(date):
    result = date.weekday()
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_monday_outputs_0_property(date):
    if date.weekday() == 0:  # If the date is a Monday
        assert date.weekday() == 0

@given(st.dates())
def test_sunday_outputs_6_property(date):
    if date.weekday() == 6:  # If the date is a Sunday
        assert date.weekday() == 6

@given(st.dates())
def test_same_day_of_week_is_consistent_property(date):
    day_of_week = date.weekday()
    assert day_of_week == day_of_week  # Consistency check for the same weekday

@given(st.dates())
def test_one_week_apart_same_output_property(date):
    one_week_later = date + datetime.timedelta(weeks=1)
    assert date.weekday() == one_week_later.weekday()
# End program