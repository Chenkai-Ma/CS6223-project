# property to violate: The mean of a dataset containing identical values must equal that value (e.g., mean([5, 5, 5]) should return 5).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) + 1  # Add 1 to the mean to violate the property
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) * 2  # Multiply the mean by 2 to violate the property
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) - 1  # Subtract 1 from the mean to violate the property
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) + 100  # Add 100 to the mean to violate the property
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) / 2  # Divide the mean by 2 to violate the property
        assert result == data[0]