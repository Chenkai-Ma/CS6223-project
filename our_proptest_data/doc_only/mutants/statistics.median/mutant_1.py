# property to violate: The median of a non-empty list of numbers should always be a number (either an integer or a float).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_1(data):
    result = "not a number"  # Violating the property by returning a string
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_2(data):
    result = None  # Violating the property by returning None
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_3(data):
    result = []  # Violating the property by returning an empty list
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_4(data):
    result = {}  # Violating the property by returning an empty dictionary
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_5(data):
    result = object()  # Violating the property by returning an object
    assert isinstance(result, (int, float))