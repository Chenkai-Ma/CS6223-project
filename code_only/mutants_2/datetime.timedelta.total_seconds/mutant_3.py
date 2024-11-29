# property to violate: The output of `total_seconds` should be proportional to the input values, meaning that doubling the input values (for `days`, `seconds`, and `microseconds`) should double the output.
from hypothesis import given, strategies as st
import datetime

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_violation_of_datetime_timedelta_total_seconds_1(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    doubled_td = datetime.timedelta(days=days * 2, seconds=seconds * 2, microseconds=microseconds * 2)
    assert td.total_seconds() * 3 == doubled_td.total_seconds()  # Violation: expected to be 2x

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_violation_of_datetime_timedelta_total_seconds_2(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    doubled_td = datetime.timedelta(days=days * 2, seconds=seconds * 2, microseconds=microseconds * 2)
    assert td.total_seconds() + 1 == doubled_td.total_seconds()  # Violation: expected to be 2x

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_violation_of_datetime_timedelta_total_seconds_3(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    doubled_td = datetime.timedelta(days=days * 2, seconds=seconds * 2, microseconds=microseconds * 2)
    assert td.total_seconds() - 1 == doubled_td.total_seconds()  # Violation: expected to be 2x

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_violation_of_datetime_timedelta_total_seconds_4(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    doubled_td = datetime.timedelta(days=days * 2, seconds=seconds * 2, microseconds=microseconds * 2)
    assert td.total_seconds() * 0.5 == doubled_td.total_seconds()  # Violation: expected to be 2x

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_violation_of_datetime_timedelta_total_seconds_5(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    doubled_td = datetime.timedelta(days=days * 2, seconds=seconds * 2, microseconds=microseconds * 2)
    assert td.total_seconds() + td.total_seconds() == doubled_td.total_seconds() + 1  # Violation: expected to be 2x