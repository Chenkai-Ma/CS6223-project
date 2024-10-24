from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2))
def test_variance_non_negative_property(data):
    result = statistics.variance(data)
    assert result >= 0

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2))
def test_variance_identical_values_property(data):
    if len(set(data)) == 1:  # All values are identical
        result = statistics.variance(data)
        assert result == 0

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2))
def test_variance_increases_with_spread_property(data):
    if len(set(data)) > 1:
        mean_original = statistics.mean(data)
        data_spread = data + [mean_original + 10]  # Increase spread
        result_original = statistics.variance(data)
        result_spread = statistics.variance(data_spread)
        assert result_spread >= result_original

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2),
               st.floats(min_value=-1e6, max_value=1e6))
def test_variance_constant_addition_property(data, constant):
    data_with_constant = [x + constant for x in data]
    result_original = statistics.variance(data)
    result_with_constant = statistics.variance(data_with_constant)
    assert result_original == result_with_constant

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2))
def test_variance_consistency_with_mean_property(data):
    mean_value = statistics.mean(data)
    variance_default = statistics.variance(data)
    variance_with_mean = statistics.variance(data, mean_value)
    assert variance_default == variance_with_mean
# End program