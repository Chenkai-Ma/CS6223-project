from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=2))
def test_output_non_negative_property(data):
    result = statistics.variance(data)
    assert result >= 0  # Variance cannot be negative

@given(st.lists(st.floats(), min_size=2))
def test_identical_values_variance_zero_property(data):
    if len(set(data)) == 1:  # All values are identical
        result = statistics.variance(data)
        assert result == 0  # Variance should be zero

@given(st.lists(st.floats(), min_size=2), st.floats())
def test_increased_spread_increases_variance_property(data, constant):
    original_variance = statistics.variance(data)
    spread_data = [x + constant for x in data]
    new_variance = statistics.variance(spread_data)
    assert new_variance >= original_variance  # Variance should not decrease

@given(st.lists(st.floats(), min_size=2), st.floats())
def test_add_constant_invariance_property(data, constant):
    original_variance = statistics.variance(data)
    shifted_data = [x + constant for x in data]
    new_variance = statistics.variance(shifted_data)
    assert new_variance == original_variance  # Adding a constant should not change variance

@given(st.lists(st.floats(), min_size=2))
def test_mean_provided_variance_consistency_property(data):
    mean_value = statistics.mean(data)
    variance_with_mean = statistics.variance(data, mean_value)
    variance_without_mean = statistics.variance(data)
    assert variance_with_mean == variance_without_mean  # Variance should be consistent

# End program