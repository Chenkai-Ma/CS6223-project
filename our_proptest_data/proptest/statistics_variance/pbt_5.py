from hypothesis import given, strategies as st
import statistics

# Property 1: The output variance should always be a non-negative value.
@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_statistics_variance_non_negative_property(data):
    result = statistics.variance(data)
    assert result >= 0

# Property 2: If the input data contains only identical values, the output variance should be zero.
@given(st.floats(), st.integers(min_value=2, max_value=100))
def test_statistics_variance_identical_values_property(value, size):
    data = [value] * size
    result = statistics.variance(data)
    assert result == 0

# Property 3: The output variance should increase if the spread of the input data increases while keeping the mean constant.
@given(st.lists(st.floats(), min_size=2), st.floats())
def test_statistics_variance_increase_with_spread_property(data, constant):
    original_variance = statistics.variance(data)
    spread_data = [x + constant for x in data]
    new_variance = statistics.variance(spread_data)
    assert new_variance >= original_variance

# Property 4: The output variance should be invariant to the addition of a constant value to all data points.
@given(st.lists(st.floats(), min_size=2), st.floats())
def test_statistics_variance_invariance_addition_property(data, constant):
    original_variance = statistics.variance(data)
    shifted_data = [x + constant for x in data]
    new_variance = statistics.variance(shifted_data)
    assert new_variance == original_variance

# Property 5: If the mean of the input data is provided as xbar, the output variance should remain consistent with the variance calculated using the automatically computed mean.
@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_statistics_variance_consistency_with_xbar_property(data):
    calculated_mean = statistics.mean(data)
    result_with_xbar = statistics.variance(data, calculated_mean)
    result_without_xbar = statistics.variance(data)
    assert result_with_xbar == result_without_xbar
# End program