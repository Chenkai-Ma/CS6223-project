# property to violate: For dates in the last week of December, the year component of the result may differ from the Gregorian year if that week belongs to the first week of the following ISO year.
from hypothesis import given, strategies as st
from datetime import date

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(d):
    if d.month == 12 and d.isocalendar()[1] == 1:  # Last week of December
        iso_year, _, _ = d.isocalendar()
        assert iso_year == d.year  # Violation: should not be equal

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(d):
    if d.month == 12 and d.isocalendar()[1] == 1:  # Last week of December
        iso_year, _, _ = d.isocalendar()
        assert iso_year > d.year  # Violation: should not be greater

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(d):
    if d.month == 12 and d.isocalendar()[1] == 1:  # Last week of December
        iso_year, _, _ = d.isocalendar()
        assert iso_year < d.year  # Violation: should not be less

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(d):
    if d.month == 12 and d.isocalendar()[1] == 1:  # Last week of December
        iso_year, _, _ = d.isocalendar()
        assert iso_year == d.year + 1  # Violation: should not be equal to year + 1

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(d):
    if d.month == 12 and d.isocalendar()[1] == 1:  # Last week of December
        iso_year, _, _ = d.isocalendar()
        assert iso_year != d.year - 1  # Violation: should not be unequal to year - 1