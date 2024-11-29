from hypothesis import given, strategies as st
import statistics
import numpy as np

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_is_number_property(data):
    result = statistics.mean(data)
    assert isinstance(result, (float, int))  # Check if the result is a number

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_identical_values_property(data):
    if len(data) > 0:
        identical_value = data[0]
        assert statistics.mean([identical_value] * len(data)) == identical_value

@given(st.lists(st.floats(), min_size=1))
def test_mean_negative_numbers_property(data):
    result = statistics.mean(data)
    assert isinstance(result, (float, int))  # Check if the result is a number
    # Check if the mean doesn't necessarily need to be negative or positive

@given()
def test_mean_empty_dataset_property():
    try:
        statistics.mean([])
        assert False  # Should not reach this line
    except statistics.StatisticsError:
        pass  # Expected behavior

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_within_range_property(data):
    result = statistics.mean(data)
    assert result >= min(data) and result <= max(data)  # Mean should be within the range
# End program