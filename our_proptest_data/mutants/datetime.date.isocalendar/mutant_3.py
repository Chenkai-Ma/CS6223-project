# property to violate: The weekday component of the result must be between 1 and 7, inclusive, where 1 represents Monday and 7 represents Sunday.
from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating the property by returning a weekday of 0
    assert 1 <= 0 <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating the property by returning a weekday of 8
    assert 1 <= 8 <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating the property by returning a weekday of -1
    assert 1 <= -1 <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating the property by returning a weekday of 10
    assert 1 <= 10 <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(d):
    _, _, iso_weekday = d.isocalendar()
    # Violating the property by returning a weekday of 15
    assert 1 <= 15 <= 7