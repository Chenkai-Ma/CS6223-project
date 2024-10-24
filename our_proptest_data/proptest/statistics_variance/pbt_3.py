from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=2))
def test_output_non_negative_property(data):
    result = statistics.variance(data)
    assert result >= 0

@given(st.lists(st.floats(), min_size=2))
def test_identical_values_zero_variance_property(data):
    if len(set(data)) == 1:  # All values are identical
        result = statistics.variance(data)
        assert result == 0

@given(st.lists(st.floats(), min_size=2))
def test_increased_spread_increases_variance_property(data):
    if len(data) > 1:
        mean_before = statistics.mean(data)
        increased_data = [value + 100 for value in data]  # Increase spread
        variance_before = statistics.variance(data)
        variance_after = statistics.variance(increased_data)
        assert variance_after >= variance_before

@given(st.lists(st.floats(), min_size=2), st.floats())
def test_constant_addition_invariance_property(data, constant):
    modified_data = [value + constant for value in data]
    variance_original = statistics.variance(data)
    variance_modified = statistics.variance(modified_data)
    assert variance_original == variance_modified

@given(st.lists(st.floats(), min_size=2))
def test_mean_argument_consistency_property(data):
    calculated_mean = statistics.mean(data)
    variance_default = statistics.variance(data)
    variance_with_mean = statistics.variance(data, calculated_mean)
    assert variance_default == variance_with_mean
# End program