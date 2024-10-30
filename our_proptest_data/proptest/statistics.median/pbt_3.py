from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=1))
def test_median_non_empty_output_is_number(data):
    result = statistics.median(data)
    assert isinstance(result, (int, float))

@given(st.lists(st.integers(), min_size=1))
def test_median_odd_length_equals_middle_element(data):
    data_sorted = sorted(data)
    if len(data_sorted) % 2 == 1:
        middle_index = len(data_sorted) // 2
        result = statistics.median(data_sorted)
        assert result == data_sorted[middle_index]

@given(st.lists(st.integers(), min_size=2))
def test_median_even_length_average_of_middle_elements(data):
    data_sorted = sorted(data)
    if len(data_sorted) % 2 == 0:
        middle_index = len(data_sorted) // 2
        result = statistics.median(data_sorted)
        average_of_middle = (data_sorted[middle_index - 1] + data_sorted[middle_index]) / 2
        assert result == average_of_middle

@given(st.lists(st.integers()))
def test_median_sorted_output_is_same(data):
    data_sorted = sorted(data)
    result_unsorted = statistics.median(data)
    result_sorted = statistics.median(data_sorted)
    assert result_unsorted == result_sorted

@given(st.lists(st.integers(), min_size=0))
def test_median_empty_input_raises_statistics_error(data):
    if len(data) == 0:
        try:
            statistics.median(data)
            assert False, "Expected StatisticsError"
        except statistics.StatisticsError:
            pass
# End program