# property to violate: The mean of a non-empty dataset should always be a numeric type (int, float, Decimal, or Fraction), depending on the input data type.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    result = "not a number"  # Violating the property by returning a string
    assert isinstance(result, (float, Decimal, Fraction))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    result = None  # Violating the property by returning None
    assert isinstance(result, (float, Decimal, Fraction))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    result = []  # Violating the property by returning an empty list
    assert isinstance(result, (float, Decimal, Fraction))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    result = {}  # Violating the property by returning an empty dictionary
    assert isinstance(result, (float, Decimal, Fraction))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    result = object()  # Violating the property by returning an arbitrary object
    assert isinstance(result, (float, Decimal, Fraction))