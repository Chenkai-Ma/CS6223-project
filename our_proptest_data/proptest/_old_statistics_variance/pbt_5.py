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

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_predictable_changes(data):
    if len(data) > 1:
        original_variance = statistics.variance(data)
        modified_data = data + [data[0] + 10]  # Adding a value far from the mean
        modified_variance = statistics.variance(modified_data)
        assert modified_variance > original_variance

@given(st.lists(st.floats(), min_size=2), st.floats())
def test_statistics_variance_with_mean(data, mean):
    result1 = statistics.variance(data)
    result2 = statistics.variance(data, mean)
    assert result1 == result2

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_increasing_spread(data):
    original_variance = statistics.variance(data)
    spread_increased_data = data + [data[0] + 20]  # Increasing spread
    modified_variance = statistics.variance(spread_increased_data)
    assert modified_variance > original_variance
# End program