# property to violate: The mean of a non-empty dataset must always be a number (integer, float, Fraction, or Decimal) and cannot be NaN or infinite.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    result = statistics.mean(data)
    result = float('nan')  # Violating the property by setting result to NaN
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    result = statistics.mean(data)
    result = float('inf')  # Violating the property by setting result to positive infinity
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    result = statistics.mean(data)
    result = -float('inf')  # Violating the property by setting result to negative infinity
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    result = statistics.mean(data)
    result = "not a number"  # Violating the property by setting result to a string
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    result = statistics.mean(data)
    result = None  # Violating the property by setting result to None
    assert isinstance(result, (float, int, Fraction, Decimal))