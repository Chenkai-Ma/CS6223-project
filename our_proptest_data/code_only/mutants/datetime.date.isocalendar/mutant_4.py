# property to violate: For any given date, if the output week is 1, then the output year should be the same as the input year or one less if the date falls before the first Monday of the year.
from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(date_input):
    year, week, day = date_input.isocalendar()
    if week == 1:
        assert year == date_input.year + 1 or (date_input.month == 1 and date_input.day <= 7 and year == date_input.year)

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(date_input):
    year, week, day = date_input.isocalendar()
    if week == 1:
        assert year == date_input.year + 2 or (date_input.month == 1 and date_input.day <= 7 and year == date_input.year)

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(date_input):
    year, week, day = date_input.isocalendar()
    if week == 1:
        assert year == date_input.year - 2 or (date_input.month == 1 and date_input.day <= 7 and year == date_input.year)

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(date_input):
    year, week, day = date_input.isocalendar()
    if week == 1:
        assert year == 9999 or (date_input.month == 1 and date_input.day <= 7 and year == date_input.year)

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(date_input):
    year, week, day = date_input.isocalendar()
    if week == 1:
        assert year == -1 or (date_input.month == 1 and date_input.day <= 7 and year == date_input.year)