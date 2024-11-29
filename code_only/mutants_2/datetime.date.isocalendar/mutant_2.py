# property to violate: The output week should always be in the range of 1 to 53, inclusive, as per ISO week date standards.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(date):
    year, week, day = date.isocalendar()
    week = 54  # Force week to be out of the valid range
    assert 1 <= week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(date):
    year, week, day = date.isocalendar()
    week = 0  # Force week to be out of the valid range
    assert 1 <= week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(date):
    year, week, day = date.isocalendar()
    week = 100  # Force week to be out of the valid range
    assert 1 <= week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(date):
    year, week, day = date.isocalendar()
    week = -1  # Force week to be out of the valid range
    assert 1 <= week <= 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(date):
    year, week, day = date.isocalendar()
    week = 60  # Force week to be out of the valid range
    assert 1 <= week <= 53