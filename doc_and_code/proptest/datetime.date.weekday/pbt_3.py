from hypothesis import given, strategies as st
import datetime

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_output_is_integer_between_0_and_6_property(date):
    result = date.weekday()
    assert 0 <= result <= 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_consistent_output_property(date):
    result1 = date.weekday()
    result2 = date.weekday()
    assert result1 == result2

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_monday_output_is_0_property(date):
    if date.weekday() == 0:  # If the date is a Monday
        assert date.weekday() == 0

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_sunday_output_is_6_property(date):
    if date.weekday() == 6:  # If the date is a Sunday
        assert date.weekday() == 6

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_cyclic_pattern_property(date):
    if date.month < 12:  # Avoid overflow to the next year
        next_day = date + datetime.timedelta(days=1)
        assert (date.weekday() + 1) % 7 == next_day.weekday()

# End program