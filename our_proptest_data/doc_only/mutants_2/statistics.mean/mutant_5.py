# property to violate: The mean of a dataset must be within the range of the minimum and maximum values of that dataset (i.e., mean(data) should be ≥ min(data) and ≤ max(data)).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    result = statistics.mean(data) + 1  # Shift the mean above the maximum
    assert result >= min(data) and result <= max(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    result = statistics.mean(data) - 1  # Shift the mean below the minimum
    assert result >= min(data) and result <= max(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    result = (max(data) + 10)  # Set the mean to a value above the maximum
    assert result >= min(data) and result <= max(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    result = (min(data) - 10)  # Set the mean to a value below the minimum
    assert result >= min(data) and result <= max(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    result = statistics.mean(data) * 2  # Scale the mean to be far above the maximum
    assert result >= min(data) and result <= max(data)