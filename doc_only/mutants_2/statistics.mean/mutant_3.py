# property to violate: The mean of a dataset that includes negative numbers must still yield a valid number, which could be negative or positive, depending on the values in the dataset.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    result = statistics.mean(data) + 1  # Shift the result to always be positive
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    result = statistics.mean(data) * 2  # Scale the result to always be positive
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    result = abs(statistics.mean(data))  # Take the absolute value to ensure it's non-negative
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    result = statistics.mean(data) if statistics.mean(data) > 0 else 0  # Force non-negative output
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    result = statistics.mean(data) + abs(statistics.mean(data))  # Ensure the result is always non-negative
    assert isinstance(result, (float, int, Fraction, Decimal))