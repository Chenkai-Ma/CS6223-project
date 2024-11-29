# property to violate: The output year should be equal to the input year if the date falls within the first week of the year; otherwise, it should reflect the correct ISO year based on the week calculation.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Incorrectly asserting that the year is always equal to the input year
        assert year == date.year

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Incorrectly asserting that the year is equal to the input year + 1
        assert year == date.year + 1

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Incorrectly asserting that the year is equal to the input year - 1
        assert year == date.year - 1

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Incorrectly asserting that the year is always a constant value (e.g., 2000)
        assert year == 2000

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Incorrectly asserting that the year is equal to the input year + 2
        assert year == date.year + 2