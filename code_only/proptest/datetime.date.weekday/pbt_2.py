from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_weekday_output_range_property(date):
    result = date.weekday()
    assert 0 <= result <= 6

@given(st.dates())
def test_weekday_output_day_mapping_property(date):
    result = date.weekday()
    # Mapping of result to days for verification
    day_mapping = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    assert result in day_mapping

@given(st.dates())
def test_weekday_consistency_property(date):
    result1 = date.weekday()
    result2 = date.weekday()
    assert result1 == result2

@given(st.dates(), st.integers())
def test_weekday_predictable_output_property(date, days_increment):
    original_weekday = date.weekday()
    new_date = date + datetime.timedelta(days=days_increment)
    new_weekday = new_date.weekday()
    assert new_weekday == (original_weekday + days_increment) % 7

@given(st.dates())
def test_weekday_periodicity_property(date):
    result1 = date.weekday()
    result2 = (date + datetime.timedelta(weeks=1)).weekday()
    assert result1 == result2
# End program