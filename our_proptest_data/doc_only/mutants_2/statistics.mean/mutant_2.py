# property to violate: The mean of a dataset containing identical values must equal that value (e.g., mean([5, 5, 5]) should return 5).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_1(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) + 1  # Modify the result to violate the property
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_2(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) * 2  # Modify the result to violate the property
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_3(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) - 1  # Modify the result to violate the property
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_4(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) + (data[0] / 2)  # Modify the result to violate the property
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_mean_5(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data) * 0  # Modify the result to violate the property
        assert result == data[0]