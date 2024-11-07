from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_is_integer_between_0_and_6_property(date):
    result = date.weekday()
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_output_represents_correct_day_of_week_property(date):
    result = date.weekday()
    assert result == (date.toordinal() + 6) % 7

@given(st.dates())
def test_result_is_consistent_for_same_date_property(date):
    result1 = date.weekday()
    result2 = date.weekday()
    assert result1 == result2

@given(st.dates())
def test_output_changes_predictably_with_input_property(date):
    next_day = date + datetime.timedelta(days=1)
    result_today = date.weekday()
    result_tomorrow = next_day.weekday()
    assert result_tomorrow == (result_today + 1) % 7

@given(st.dates())
def test_output_exhibits_periodicity_property(date):
    one_week_later = date + datetime.timedelta(weeks=1)
    result_today = date.weekday()
    result_next_week = one_week_later.weekday()
    assert result_today == result_next_week
# End program