from hypothesis import given, strategies as st
from statistics import variance, StatisticsError

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_non_negative(data):
    result = variance(data)
    assert result >= 0

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_identical_values(data):
    if len(set(data)) == 1:  # All values are identical
        result = variance(data)
        assert result == 0

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_predictable_modification(data):
    original_variance = variance(data)
    modified_data = data + [1000.0]  # Add a large outlier
    modified_variance = variance(modified_data)
    assert modified_variance >= original_variance  # Variance should increase

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_mean_argument(data):
    mean_value = sum(data) / len(data)
    result_with_mean = variance(data, mean_value)
    result_without_mean = variance(data)
    assert result_with_mean == result_without_mean  # Both should be equal

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_spread(data):
    original_variance = variance(data)
    spread_data = data + [original_variance * 10]  # Increase spread
    spread_variance = variance(spread_data)
    assert spread_variance >= original_variance  # Variance should increase with spread
# End program