# property to violate: The output of the function is always an integer between 0 and 6, inclusive.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1():
    result = datetime.date(2021, 1, 1).weekday() + 10  # Always returns 10, violating the property
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_2():
    result = datetime.date(2021, 1, 1).weekday() - 1  # Always returns -1, violating the property
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_3():
    result = datetime.date(2021, 1, 1).weekday() * 2  # Will return values like 0, 2, 4, 6, 8, 10, violating the property
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_4():
    result = 7  # Always returns 7, violating the property
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_5():
    result = -5  # Always returns -5, violating the property
    assert isinstance(result, int) and 0 <= result <= 6