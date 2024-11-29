from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_is_integer_between_0_and_6_property(date):
    result = date.weekday()
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_output_is_consistent_property(date):
    result1 = date.weekday()
    result2 = date.weekday()
    assert result1 == result2

@given(st.dates())
def test_monday_output_is_0_property(date):
    if date.weekday() == 0:  # If the date is a Monday
        assert date.weekday() == 0

@given(st.dates())
def test_sunday_output_is_6_property(date):
    if date.weekday() == 6:  # If the date is a Sunday
        assert date.weekday() == 6

@given(st.dates())
def test_cyclic_pattern_property(date):
    weekday_output = date.weekday()
    next_day = date + datetime.timedelta(days=1)
    next_weekday_output = next_day.weekday()
    assert (next_weekday_output - weekday_output) % 7 == 1
# End program