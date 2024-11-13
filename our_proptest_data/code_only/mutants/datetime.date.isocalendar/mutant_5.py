# property to violate: If the input date is the last day of the year (December 31), the output week should either be the last week of the year or the first week of the following year, depending on whether it falls before or after the first Monday of the new year.
from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(date_input):
    if date_input.month == 12 and date_input.day == 31:
        # Incorrectly forcing the week to be 2 regardless of the actual week
        year, week, day = date_input.isocalendar()
        assert year == date_input.year + 1 or week == 2

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(date_input):
    if date_input.month == 12 and date_input.day == 31:
        # Incorrectly forcing the week to be 53 for all last days of the year
        year, week, day = date_input.isocalendar()
        assert year == date_input.year + 1 or week == 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(date_input):
    if date_input.month == 12 and date_input.day == 31:
        # Incorrectly forcing the year to be the same year instead of the next year
        year, week, day = date_input.isocalendar()
        assert year == date_input.year or week == 53

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(date_input):
    if date_input.month == 12 and date_input.day == 31:
        # Incorrectly forcing the week to be 51 regardless of actual week
        year, week, day = date_input.isocalendar()
        assert year == date_input.year + 1 or week == 51

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(date_input):
    if date_input.month == 12 and date_input.day == 31:
        # Incorrectly forcing the week to be 0 for all last days of the year
        year, week, day = date_input.isocalendar()
        assert year == date_input.year + 1 or week == 0