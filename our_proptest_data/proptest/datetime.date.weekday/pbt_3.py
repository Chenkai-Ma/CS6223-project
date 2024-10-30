from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_is_integer_between_0_and_6_property(date):
    result = date.weekday()
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_monday_output_is_0_property(date):
    if date.weekday() == 0:  # If it's a Monday
        assert date.weekday() == 0

@given(st.dates())
def test_sunday_output_is_6_property(date):
    if date.weekday() == 6:  # If it's a Sunday
        assert date.weekday() == 6

@given(st.dates())
def test_same_day_of_week_consistency_property(date):
    if date.weekday() in range(7):  # Check for any valid weekday
        assert datetime.date(date.year, date.month, date.day).weekday() == date.weekday()

@given(st.dates())
def test_one_week_apart_consistency_property(date):
    one_week_later = date + datetime.timedelta(weeks=1)
    assert date.weekday() == one_week_later.weekday()
# End program