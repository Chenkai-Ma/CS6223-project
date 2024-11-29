# property to violate: The output year should be equal to the input year if the date falls within the first week of the year; otherwise, it should reflect the correct ISO year based on the week calculation.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(date):
    year, week, day = date.isocalendar()
    if week == 1:
        assert year == date.year + 1  # Incorrectly asserting that the year is one more than the input year.

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(date):
    year, week, day = date.isocalendar()
    if week == 1:
        assert year == date.year - 2  # Incorrectly asserting that the year is two less than the input year.

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(date):
    year, week, day = date.isocalendar()
    if week == 1:
        assert year == 9999  # Incorrectly asserting that the year is always 9999 for the first week.

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(date):
    year, week, day = date.isocalendar()
    if week == 1:
        assert year == 2023  # Incorrectly asserting that the year is always 2023 for the first week.

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(date):
    year, week, day = date.isocalendar()
    if week == 1:
        assert year == date.year + 10  # Incorrectly asserting that the year is ten more than the input year.