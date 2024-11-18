# property to violate: The year component of the result must be equal to the Gregorian year of the date if the date falls within the first week of the ISO year (i.e., the week containing the first Thursday of the year).
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_1(d):
    iso_year, _, _ = d.isocalendar()
    if d.isocalendar()[1] == 1:  # Checking for the first week
        assert iso_year != d.year  # Violation: asserting inequality

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_2(d):
    iso_year, _, _ = d.isocalendar()
    if d.isocalendar()[1] == 1:  # Checking for the first week
        assert iso_year == d.year + 1  # Violation: asserting iso_year is one more than d.year

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_3(d):
    iso_year, _, _ = d.isocalendar()
    if d.isocalendar()[1] == 1:  # Checking for the first week
        assert iso_year == d.year - 1  # Violation: asserting iso_year is one less than d.year

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_4(d):
    iso_year, _, _ = d.isocalendar()
    if d.isocalendar()[1] == 1:  # Checking for the first week
        assert iso_year == 9999  # Violation: asserting iso_year to a fixed incorrect value

@given(st.dates())
def test_violation_of_datetime_date_isocalendar_5(d):
    iso_year, _, _ = d.isocalendar()
    if d.isocalendar()[1] == 1:  # Checking for the first week
        assert iso_year == -1  # Violation: asserting iso_year to an invalid negative value