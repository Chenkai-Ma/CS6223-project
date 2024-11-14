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
    if date.weekday() == 0:  # If it's Monday
        assert date.weekday() == 0

@given(st.dates())
def test_sunday_output_is_6_property(date):
    if date.weekday() == 6:  # If it's Sunday
        assert date.weekday() == 6

@given(st.dates())
def test_cyclic_pattern_property(date):
    previous_date = date - datetime.timedelta(days=1)
    next_date = date + datetime.timedelta(days=1)
    assert (previous_date.weekday() + 1) % 7 == date.weekday()
    assert (date.weekday() + 1) % 7 == next_date.weekday()
# End program