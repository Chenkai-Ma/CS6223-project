# property to violate: The output day should always be in the range of 1 to 7, corresponding to Monday through Sunday.
from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(date_input):
    year, week, day = date_input.isocalendar()
    day = 0  # Violating the property by setting day to 0
    assert 1 <= day <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(date_input):
    year, week, day = date_input.isocalendar()
    day = 8  # Violating the property by setting day to 8
    assert 1 <= day <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(date_input):
    year, week, day = date_input.isocalendar()
    day = -1  # Violating the property by setting day to -1
    assert 1 <= day <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(date_input):
    year, week, day = date_input.isocalendar()
    day = 10  # Violating the property by setting day to 10
    assert 1 <= day <= 7

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(date_input):
    year, week, day = date_input.isocalendar()
    day = 15  # Violating the property by setting day to 15
    assert 1 <= day <= 7