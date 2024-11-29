# property to violate: The output of `total_seconds` should equal zero if both `days`, `seconds`, and `microseconds` are all zero.
from hypothesis import given, strategies as st
import datetime

@given(st.data())
def test_violation_of_datetime_timedelta_total_seconds_1():
    td = datetime.timedelta(days=0, seconds=0, microseconds=0)
    assert td.total_seconds() != 0  # Violating the property by asserting not equal to 0

@given(st.data())
def test_violation_of_datetime_timedelta_total_seconds_2():
    td = datetime.timedelta(days=0, seconds=0, microseconds=0)
    assert td.total_seconds() == 1  # Violating the property by asserting equal to 1

@given(st.data())
def test_violation_of_datetime_timedelta_total_seconds_3():
    td = datetime.timedelta(days=0, seconds=0, microseconds=0)
    assert td.total_seconds() == -1  # Violating the property by asserting equal to -1

@given(st.data())
def test_violation_of_datetime_timedelta_total_seconds_4():
    td = datetime.timedelta(days=0, seconds=0, microseconds=0)
    assert td.total_seconds() == 100  # Violating the property by asserting equal to 100

@given(st.data())
def test_violation_of_datetime_timedelta_total_seconds_5():
    td = datetime.timedelta(days=0, seconds=0, microseconds=0)
    assert td.total_seconds() == 999999  # Violating the property by asserting equal to 999999