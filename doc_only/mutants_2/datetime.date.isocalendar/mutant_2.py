# property to violate: The week component of the result must be between 1 and 53, inclusive, as the ISO calendar can have either 52 or 53 weeks in a year.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(d):
    # Force the week to be less than 1
    _, iso_week, _ = d.isocalendar()
    iso_week = 0  # This violates the property
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(d):
    # Force the week to be greater than 53
    _, iso_week, _ = d.isocalendar()
    iso_week = 54  # This violates the property
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(d):
    # Force the week to be less than 1
    _, iso_week, _ = d.isocalendar()
    iso_week = -1  # This violates the property
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(d):
    # Force the week to be greater than 53
    _, iso_week, _ = d.isocalendar()
    iso_week = 100  # This violates the property
    assert 1 <= iso_week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(d):
    # Force the week to be less than 1
    _, iso_week, _ = d.isocalendar()
    iso_week = -10  # This violates the property
    assert 1 <= iso_week <= 53