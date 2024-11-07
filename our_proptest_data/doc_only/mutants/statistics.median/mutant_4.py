# property to violate: The median should raise a StatisticsError when the input list is empty.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_1(data):
    if len(data) == 0:
        # Incorrectly returning a value instead of raising an error
        return 0  # This should not happen, we expect an error

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_2(data):
    if len(data) == 0:
        # Incorrectly returning None instead of raising an error
        return None  # This should not happen, we expect an error

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_3(data):
    if len(data) == 0:
        # Incorrectly returning a string instead of raising an error
        return "No data"  # This should not happen, we expect an error

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_4(data):
    if len(data) == 0:
        # Incorrectly returning an empty list instead of raising an error
        return []  # This should not happen, we expect an error

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_5(data):
    if len(data) == 0:
        # Incorrectly raising a different exception instead of StatisticsError
        raise ValueError("This is not the expected error")  # This should not happen, we expect an error