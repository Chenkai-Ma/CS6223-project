# property to violate: The mean of a non-empty dataset must always be a number (integer, float, Fraction, or Decimal) and cannot be NaN or infinite.
from hypothesis import given, strategies as st
import statistics
from fractions import Fraction
from decimal import Decimal
import math

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    result = math.nan  # Setting result to NaN to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    result = float('inf')  # Setting result to positive infinity to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    result = float('-inf')  # Setting result to negative infinity to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    result = None  # Setting result to None to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    result = "not a number"  # Setting result to a string to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))