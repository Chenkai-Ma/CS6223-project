from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_non_negative(data):
    result = statistics.variance(data)
    assert result >= 0

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_identical_values(data):
    if all(x == data[0] for x in data):
        result = statistics.variance(data)
        assert result == 0

@given(st.lists(st.floats(), min_size=2), st.floats())
def test_statistics_variance_increasing_spread(data, new_value):
    original_variance = statistics.variance(data)
    modified_data = data + [new_value]
    modified_variance = statistics.variance(modified_data)
    assert modified_variance >= original_variance

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_consistent_mean(data):
    calculated_mean = statistics.mean(data)
    variance_with_mean = statistics.variance(data, calculated_mean)
    variance_without_mean = statistics.variance(data)
    assert variance_with_mean == variance_without_mean

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_spread_relationship(data):
    original_variance = statistics.variance(data)
    modified_data = data + [data[0] + 1000]  # Adding a value far from the mean
    modified_variance = statistics.variance(modified_data)
    assert modified_variance > original_variance
# End program