# property to violate: The mean of a dataset must be within the range of the minimum and maximum values of that dataset (i.e., mean(data) should be ≥ min(data) and ≤ max(data)).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    result = statistics.mean(data) + 1  # Shift mean above max(data)
    assert result >= min(data) and result <= max(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    result = statistics.mean(data) - 1  # Shift mean below min(data)
    assert result >= min(data) and result <= max(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    result = (statistics.mean(data) + max(data) + 1) / 2  # Mean is forced above max(data)
    assert result >= min(data) and result <= max(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    result = (statistics.mean(data) + min(data) - 1) / 2  # Mean is forced below min(data)
    assert result >= min(data) and result <= max(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    result = statistics.mean(data) + (max(data) - min(data) + 1)  # Shift mean far above max(data)
    assert result >= min(data) and result <= max(data)