from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(min_value=-1000000, max_value=1000000), min_size=1))
def test_median_non_empty_output_is_number_property(data):
    result = statistics.median(data)
    assert isinstance(result, (int, float))

@given(st.lists(st.integers(min_value=-1000000, max_value=1000000), min_size=1))
def test_median_odd_length_is_middle_element_property(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == sorted_data[len(sorted_data) // 2]

@given(st.lists(st.integers(min_value=-1000000, max_value=1000000), min_size=2))
def test_median_even_length_is_average_of_middle_elements_property(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        mid_index = len(sorted_data) // 2
        expected_result = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
        result = statistics.median(sorted_data)
        assert result == expected_result

@given(st.lists(st.integers(min_value=-1000000, max_value=1000000)))
def test_median_sorted_input_is_same_property(data):
    sorted_data = sorted(data)
    result_unsorted = statistics.median(data)
    result_sorted = statistics.median(sorted_data)
    assert result_unsorted == result_sorted

@given(st.lists(st.integers(min_value=-1000000, max_value=1000000), min_size=0))
def test_median_empty_input_raises_statistics_error_property(data):
    if len(data) == 0:
        try:
            statistics.median(data)
            assert False, "Expected StatisticsError not raised"
        except statistics.StatisticsError:
            pass  # Test passes
# End program