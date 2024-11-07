# property to violate: The weekday component of the result must be between 1 and 7, inclusive, where 1 represents Monday and 7 represents Sunday.
from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating by returning a weekday less than 1
    assert 1 <= iso_weekday - 2 <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating by returning a weekday greater than 7
    assert 1 <= iso_weekday + 2 <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating by returning a weekday equal to 0
    assert 1 <= iso_weekday - iso_weekday <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating by returning a weekday equal to 8
    assert 1 <= iso_weekday + 1 <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating by returning a weekday less than 1 and greater than 7
    assert 1 <= iso_weekday - 10 <= 7