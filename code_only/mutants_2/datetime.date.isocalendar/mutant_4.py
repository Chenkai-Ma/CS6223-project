# property to violate: For any given date, if the output week is 1, then the output year should be the same as the input year or one less if the date falls before the first Monday of the year.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Violate by changing the year to be two years less than the input year
        assert (year - 2) == date.year or (date.month == 1 and date.day <= 7 and (year - 2) == date.year - 1)

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Violate by changing the year to a fixed incorrect value
        assert 9999 == date.year or (date.month == 1 and date.day <= 7 and 9999 == date.year - 1)

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Violate by making the year equal to the input year plus one
        assert (year + 1) == date.year or (date.month == 1 and date.day <= 7 and (year + 1) == date.year - 1)

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Violate by making the year equal to the input year minus three
        assert (year - 3) == date.year or (date.month == 1 and date.day <= 7 and (year - 3) == date.year - 1)

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(date):
    year, week, day = date.isocalendar()
    if week == 1:
        # Violate by making the year equal to the input year plus two
        assert (year + 2) == date.year or (date.month == 1 and date.day <= 7 and (year + 2) == date.year - 1)