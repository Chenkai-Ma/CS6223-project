from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_is_integer_between_0_and_6_property(date):
    assert 0 <= date.weekday() <= 6

@given(st.dates())
def test_output_is_consistent_property(date):
    assert date.weekday() == date.weekday()

@given(st.dates())
def test_monday_output_is_0_property(date):
    if date.weekday() == 0:  # Monday
        assert date.weekday() == 0

@given(st.dates())
def test_sunday_output_is_6_property(date):
    if date.weekday() == 6:  # Sunday
        assert date.weekday() == 6

@given(st.dates())
def test_cyclic_pattern_property(date):
    if date.weekday() < 6:  # Not Sunday
        assert date.weekday() + 1 == (date + datetime.timedelta(days=1)).weekday() % 7
    else:  # Sunday
        assert (date.weekday() + 1) % 7 == (date + datetime.timedelta(days=1)).weekday()
# End program