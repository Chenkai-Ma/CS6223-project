# property to violate: The output of the function is always an integer between 0 and 6, inclusive.
from hypothesis import given, strategies as st
import datetime

@given(st.dates())
def test_violation_of_datetime_date_weekday_1():
    result = datetime.date(2021, 1, 1).weekday() + 10  # Adding 10 to ensure the result is always greater than 6
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_2():
    result = datetime.date(2021, 1, 1).weekday() - 1  # Subtracting 1 to ensure the result is always less than 0
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_3():
    result = str(datetime.date(2021, 1, 1).weekday())  # Changing the result to a string
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_4():
    result = datetime.date(2021, 1, 1).weekday() * 2  # Multiplying by 2 to ensure the result can exceed 6
    assert isinstance(result, int) and 0 <= result <= 6

@given(st.dates())
def test_violation_of_datetime_date_weekday_5():
    result = None  # Setting the result to None
    assert isinstance(result, int) and 0 <= result <= 6