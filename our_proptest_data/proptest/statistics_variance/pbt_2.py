from hypothesis import given, strategies as st
import statistics
import numpy as np

@given(st.lists(st.floats(), min_size=2))
def test_statistics_variance_property(data):
    # Property 1: Variance should be non-negative
    var = statistics.variance(data)
    assert var >= 0

    # Property 2: If all values are the same, variance should be zero
    if all(x == data[0] for x in data):
        assert statistics.variance(data) == 0

    # Property 3: Variance should change predictably with modifications
    original_variance = statistics.variance(data)
    modified_data = data + [max(data) + 1000]  # Adding a far value
    modified_variance = statistics.variance(modified_data)
    assert modified_variance >= original_variance  # Should increase with spread

    # Property 4: Consistency of variance with provided mean
    mean_value = np.mean(data)
    assert statistics.variance(data, mean_value) == original_variance

    # Property 5: Variance should reflect increased spread
    wider_data = data + [max(data) + 1000, min(data) - 1000]  # Adding far values
    wider_variance = statistics.variance(wider_data)
    assert wider_variance > original_variance  # Should increase due to added spread
# End program