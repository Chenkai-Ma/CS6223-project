# property to violate: The week component of the result must be between 1 and 53, inclusive, as the ISO calendar can have either 52 or 53 weeks in a year.
from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(d):
    _, iso_week, _ = d.isocalendar()
    # Force the week to be below 1
    iso_week = 0
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(d):
    _, iso_week, _ = d.isocalendar()
    # Force the week to be above 53
    iso_week = 54
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(d):
    _, iso_week, _ = d.isocalendar()
    # Force the week to be negative
    iso_week = -1
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(d):
    _, iso_week, _ = d.isocalendar()
    # Force the week to be a large number
    iso_week = 100
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(d):
    _, iso_week, _ = d.isocalendar()
    # Force the week to be a non-integer (e.g., float)
    iso_week = 52.5
    assert 1 <= iso_week <= 53