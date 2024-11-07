# property to violate: The mean of a dataset that includes negative numbers must still yield a valid number, which could be negative or positive, depending on the values in the dataset.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    result = statistics.mean(data)
    # Always return a fixed invalid number (e.g., 9999) to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))
    result = 9999

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    result = statistics.mean(data)
    # Always return a fixed negative number (e.g., -9999) to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))
    result = -9999

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    result = statistics.mean(data)
    # Always return None to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))
    result = None

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    result = statistics.mean(data)
    # Always return a string to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))
    result = "invalid"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    result = statistics.mean(data)
    # Always return an empty list to violate the property
    assert isinstance(result, (float, int, Fraction, Decimal))
    result = []