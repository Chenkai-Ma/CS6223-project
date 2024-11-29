# property to violate: The mean of a dataset that includes negative numbers must still yield a valid number, which could be negative or positive, depending on the values in the dataset.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    result = statistics.mean(data)
    # Force result to be an invalid number (e.g., NaN)
    result = float('nan')
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    result = statistics.mean(data)
    # Force result to be a string (invalid type)
    result = "invalid"
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    result = statistics.mean(data)
    # Force result to be a complex number (invalid type)
    result = 1 + 2j
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    result = statistics.mean(data)
    # Force result to be a list (invalid type)
    result = [1, 2, 3]
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    result = statistics.mean(data)
    # Force result to be None (invalid type)
    result = None
    assert isinstance(result, (float, int, Fraction, Decimal))