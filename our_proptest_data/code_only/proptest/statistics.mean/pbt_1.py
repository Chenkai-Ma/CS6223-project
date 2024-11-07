from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=1))
def test_mean_identical_elements_property(data):
    if len(data) > 0:
        identical_value = data[0]
        mean_value = statistics.mean([identical_value] * len(data))
        assert mean_value == identical_value

@given(st.lists(st.floats(), max_size=100))
def test_mean_empty_list_property(data):
    if len(data) == 0:
        try:
            statistics.mean(data)
            assert False, "Expected StatisticsError for empty list"
        except statistics.StatisticsError:
            pass  # Expected exception

@given(st.lists(st.floats(), min_size=1))
def test_mean_range_property(data):
    mean_value = statistics.mean(data)
    assert mean_value >= min(data) and mean_value <= max(data)

@given(st.lists(st.floats(), max_size=100))
def test_mean_invariant_under_zero_property(data):
    mean_value = statistics.mean(data)
    mean_value_with_zero = statistics.mean(data + [0])
    assert mean_value == mean_value_with_zero

@given(st.lists(st.floats(), min_size=1), st.lists(st.floats(), min_size=1))
def test_mean_concatenated_lists_property(data1, data2):
    mean1 = statistics.mean(data1)
    mean2 = statistics.mean(data2)
    combined_data = data1 + data2
    if len(combined_data) > 0:
        combined_mean = statistics.mean(combined_data)
        weighted_mean = (mean1 * len(data1) + mean2 * len(data2)) / (len(data1) + len(data2))
        assert combined_mean == pytest.approx(weighted_mean)

# End program