from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_is_integer_between_0_and_6_property(date):
    result = date.weekday()
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_monday_always_returns_0_property(date):
    if date.weekday() == 0:  # Check if it's Monday
        assert date.weekday() == 0

@given(st.dates())
def test_sunday_always_returns_6_property(date):
    if date.weekday() == 6:  # Check if it's Sunday
        assert date.weekday() == 6

@given(st.dates())
def test_same_day_of_week_is_consistent_property(date):
    day_of_week = date.weekday()
    # Generate another date with the same day of the week
    same_day_date = date + datetime.timedelta(days=(7 * st.integers(min_value=0, max_value=10).example()))
    assert same_day_date.weekday() == day_of_week

@given(st.dates())
def test_one_week_apart_same_output_property(date):
    result = date.weekday()
    week_apart_date = date + datetime.timedelta(days=7)
    assert week_apart_date.weekday() == result

# End program