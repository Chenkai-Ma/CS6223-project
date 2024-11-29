# property to violate: The output should increase if the variability of the input data increases (i.e., if the range of the input data expands).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_1(data):
    if len(data) > 1:
        original_variance = statistics.pstdev(data)
        expanded_data = data + [max(data) + 10]  # Adding an outlier to increase variability
        result = statistics.pstdev(expanded_data) - 1  # Decrease the result to violate the property
        assert result >= original_variance

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_2(data):
    if len(data) > 1:
        original_variance = statistics.pstdev(data)
        expanded_data = data + [max(data) + 10]  # Adding an outlier to increase variability
        result = statistics.pstdev(expanded_data) * 0.5  # Halve the result to violate the property
        assert result >= original_variance

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_3(data):
    if len(data) > 1:
        original_variance = statistics.pstdev(data)
        expanded_data = data + [max(data) + 10]  # Adding an outlier to increase variability
        result = -statistics.pstdev(expanded_data)  # Negate the result to violate the property
        assert result >= original_variance

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_4(data):
    if len(data) > 1:
        original_variance = statistics.pstdev(data)
        expanded_data = data + [max(data) + 10]  # Adding an outlier to increase variability
        result = statistics.pstdev(expanded_data) + 100  # Add a large constant to violate the property
        assert result >= original_variance

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_5(data):
    if len(data) > 1:
        original_variance = statistics.pstdev(data)
        expanded_data = data + [max(data) + 10]  # Adding an outlier to increase variability
        result = statistics.pstdev(expanded_data) - (original_variance + 1)  # Subtract more than original to violate the property
        assert result >= original_variance