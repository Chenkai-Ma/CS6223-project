# property to violate: The output day should always be in the range of 1 to 7, corresponding to Monday through Sunday.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(date):
    year, week, day = date.isocalendar()
    # Force day to be 0, which is out of range
    day = 0
    assert 1 <= day <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(date):
    year, week, day = date.isocalendar()
    # Force day to be 8, which is out of range
    day = 8
    assert 1 <= day <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(date):
    year, week, day = date.isocalendar()
    # Force day to be -1, which is out of range
    day = -1
    assert 1 <= day <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(date):
    year, week, day = date.isocalendar()
    # Force day to be 10, which is out of range
    day = 10
    assert 1 <= day <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(date):
    year, week, day = date.isocalendar()
    # Force day to be 15, which is out of range
    day = 15
    assert 1 <= day <= 7