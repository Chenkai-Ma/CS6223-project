# property to violate: The output of the function is always an integer between 0 and 6, inclusive.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1():
    result = datetime.date.weekday(datetime.date(2000, 1, 1)) + 10  # Shift result to be greater than 6
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_2():
    result = datetime.date.weekday(datetime.date(2000, 1, 1)) - 10  # Shift result to be less than 0
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_3():
    result = datetime.date.weekday(datetime.date(2000, 1, 1)) + 100  # Shift result to be well above 6
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_4():
    result = datetime.date.weekday(datetime.date(2000, 1, 1)) - 100  # Shift result to be well below 0
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_5():
    result = float(datetime.date.weekday(datetime.date(2000, 1, 1)))  # Change result type to float
    assert isinstance(result, int) and 0 <= result <= 6