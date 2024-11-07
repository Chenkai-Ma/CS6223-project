from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_weekday_output_range_property(date):
    result = date.weekday()
    assert 0 <= result <= 6

@given(st.dates())
def test_weekday_correct_day_of_week_property(date):
    result = date.weekday()
    # Mapping: 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
    expected_day = (date.toordinal() + 6) % 7
    assert result == expected_day

@given(st.dates())
def test_weekday_consistency_property(date):
    result1 = date.weekday()
    result2 = date.weekday()
    assert result1 == result2

@given(st.dates())
def test_weekday_predictable_change_property(date):
    result_today = date.weekday()
    tomorrow = date + datetime.timedelta(days=1)
    result_tomorrow = tomorrow.weekday()
    assert result_tomorrow == (result_today + 1) % 7

@given(st.dates())
def test_weekday_periodicity_property(date):
    result_today = date.weekday()
    one_week_later = date + datetime.timedelta(weeks=1)
    result_one_week_later = one_week_later.weekday()
    assert result_today == result_one_week_later
# End program