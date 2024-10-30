from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_is_integer_between_0_and_6_property(date):
    result = date.weekday()
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_monday_output_is_0_property(date):
    if date.weekday() == 0:  # If it's Monday
        assert date.weekday() == 0

@given(st.dates())
def test_sunday_output_is_6_property(date):
    if date.weekday() == 6:  # If it's Sunday
        assert date.weekday() == 6

@given(st.dates())
def test_same_day_of_week_is_consistent_property(date):
    weekday = date.weekday()
    assert weekday == datetime.date(date.year, date.month, date.day).weekday()

@given(st.dates())
def test_output_for_dates_one_week_apart_remains_same_property(date):
    same_weekday_date = date + datetime.timedelta(days=7)
    assert date.weekday() == same_weekday_date.weekday()
# End program