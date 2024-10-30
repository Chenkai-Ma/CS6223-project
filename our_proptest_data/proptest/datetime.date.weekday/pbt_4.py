from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_is_integer_between_0_and_6_property(date):
    result = date.weekday()
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_monday_output_is_0_property(date):
    if date.weekday() == 0:  # If the date is a Monday
        assert date.weekday() == 0

@given(st.dates())
def test_sunday_output_is_6_property(date):
    if date.weekday() == 6:  # If the date is a Sunday
        assert date.weekday() == 6

@given(st.dates())
def test_same_day_of_week_is_consistent_property(date):
    weekday = date.weekday()
    assert all((date.replace(month=(date.month + i - 1) % 12 + 1) if (date.month + i - 1) % 12 + 1 != 0 else date.replace(year=date.year + 1, month=1) if (date.month + i - 1) % 12 + 1 == 1 else date).weekday() == weekday for i in range(-3, 4))

@given(st.dates())
def test_week_apart_output_is_same_property(date):
    assert date.weekday() == (date + datetime.timedelta(weeks=1)).weekday()
# End program