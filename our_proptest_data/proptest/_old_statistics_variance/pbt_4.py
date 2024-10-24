from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_property(data):
    # Property 1: Variance should be non-negative
    var = statistics.variance(data)
    assert var >= 0

    # Property 2: Identical values should result in zero variance
    if all(x == data[0] for x in data):
        assert statistics.variance(data) == 0

    # Property 3: Adding a value far from the mean should increase variance
    original_variance = statistics.variance(data)
    modified_data = data + [max(data) + 1000]  # Adding a value far from the mean
    modified_variance = statistics.variance(modified_data)
    assert modified_variance >= original_variance  # Variance should not decrease

    # Property 4: Providing the correct mean should yield the same variance
    mean_value = statistics.mean(data)
    assert statistics.variance(data, mean_value) == var

    # Property 5: Increasing spread should increase variance
    wide_data = data + [min(data) - 1000]  # Adding a value far below the mean
    wide_variance = statistics.variance(wide_data)
    assert wide_variance >= var  # Variance should not decrease
# End program