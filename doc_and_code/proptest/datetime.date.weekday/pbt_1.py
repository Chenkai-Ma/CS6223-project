from hypothesis import given, strategies as st
import datetime

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_output_range_property(date):
    result = date.weekday()
    assert 0 <= result <= 6
# End program

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_consistency_property(date):
    result1 = date.weekday()
    result2 = date.weekday()
    assert result1 == result2
# End program

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_monday_property(date):
    if date.weekday() == 0:  # If it's Monday
        assert date.weekday() == 0
# End program

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_sunday_property(date):
    if date.weekday() == 6:  # If it's Sunday
        assert date.weekday() == 6
# End program

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_cyclic_pattern_property(date):
    next_day = date + datetime.timedelta(days=1)
    assert (date.weekday() + 1) % 7 == next_day.weekday()
# End program