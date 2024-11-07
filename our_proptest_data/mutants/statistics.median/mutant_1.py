# property to violate: The median of a non-empty list of numbers should always be a number (either an integer or a float).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_1(data):
    result = statistics.median(data)
    result = None  # Changing the output to None, which is not a number
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_2(data):
    result = statistics.median(data)
    result = "not a number"  # Changing the output to a string
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_3(data):
    result = statistics.median(data)
    result = [1, 2, 3]  # Changing the output to a list
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_4(data):
    result = statistics.median(data)
    result = {1: "one", 2: "two"}  # Changing the output to a dictionary
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_5(data):
    result = statistics.median(data)
    result = complex(1, 1)  # Changing the output to a complex number
    assert isinstance(result, (int, float))