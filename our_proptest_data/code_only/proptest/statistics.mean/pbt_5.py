from hypothesis import given, strategies as st
from statistics import mean, StatisticsError

@given(st.lists(st.floats(), min_size=1))
def test_mean_identical_elements_property(data):
    if len(data) > 0:
        identical_value = data[0]
        assert mean([identical_value] * len(data)) == identical_value

@given(st.lists(st.floats(), min_size=0))
def test_mean_empty_list_property(data):
    if len(data) == 0:
        try:
            mean(data)
            assert False, "Expected StatisticsError for empty list"
        except StatisticsError:
            pass

@given(st.lists(st.floats(), min_size=1))
def test_mean_range_property(data):
    calculated_mean = mean(data)
    assert min(data) <= calculated_mean <= max(data)

@given(st.lists(st.floats(), min_size=1))
def test_mean_invariant_zero_property(data):
    original_mean = mean(data)
    assert mean(data + [0]) == original_mean

@given(st.lists(st.floats(), min_size=1), st.lists(st.floats(), min_size=1))
def test_mean_concatenated_lists_property(data1, data2):
    combined_data = data1 + data2
    if combined_data:
        mean_combined = mean(combined_data)
        mean_data1 = mean(data1)
        mean_data2 = mean(data2)
        weighted_mean = (mean_data1 * len(data1) + mean_data2 * len(data2)) / (len(data1) + len(data2))
        assert mean_combined == weighted_mean

# End program