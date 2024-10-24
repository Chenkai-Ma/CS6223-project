from hypothesis import given, strategies as st

@given(st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_variance_property(data):
    original_variance = statistics.variance(data)
    modified_data = data + [data[0] - 1000]  # Adding a value that is significantly lower than the mean
    modified_variance = statistics.variance(modified_data)
    assert modified_variance < original_variance  # This violates the property
# End program