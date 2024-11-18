# property to violate: The weekday component of the result must be between 1 and 7, inclusive, where 1 represents Monday and 7 represents Sunday.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(d):
    _, _, iso_weekday = d.isocalendar()
    iso_weekday = 0  # Violating the property by setting weekday to 0
    assert 1 <= iso_weekday <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(d):
    _, _, iso_weekday = d.isocalendar()
    iso_weekday = 8  # Violating the property by setting weekday to 8
    assert 1 <= iso_weekday <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(d):
    _, _, iso_weekday = d.isocalendar()
    iso_weekday = -1  # Violating the property by setting weekday to -1
    assert 1 <= iso_weekday <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(d):
    _, _, iso_weekday = d.isocalendar()
    iso_weekday = 10  # Violating the property by setting weekday to 10
    assert 1 <= iso_weekday <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(d):
    _, _, iso_weekday = d.isocalendar()
    iso_weekday = 15  # Violating the property by setting weekday to 15
    assert 1 <= iso_weekday <= 7