from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_output_is_integer_between_0_and_6_property(date):
    result = date.weekday()
    assert isinstance(result, int)
    assert 0 <= result <= 6

@given(st.dates())
def test_output_represents_correct_day_of_week_property(date):
    result = date.weekday()
    # Check mapping: 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
    expected = (date.toordinal() + 6) % 7
    assert result == expected

@given(st.dates())
def test_result_is_consistent_for_same_date_property(date):
    result1 = date.weekday()
    result2 = date.weekday()
    assert result1 == result2

@given(st.dates())
def test_output_changes_predictably_with_input_increment_property(date):
    next_day = date + datetime.timedelta(days=1)
    result_today = date.weekday()
    result_next_day = next_day.weekday()
    assert result_next_day == (result_today + 1) % 7

@given(st.dates())
def test_output_exhibits_periodicity_property(date):
    result_today = date.weekday()
    one_week_later = date + datetime.timedelta(weeks=1)
    result_one_week_later = one_week_later.weekday()
    assert result_today == result_one_week_later
# End program