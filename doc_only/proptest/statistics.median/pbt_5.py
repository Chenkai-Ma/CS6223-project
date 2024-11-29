from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=1))
def test_median_returns_number_property(data):
    result = statistics.median(data)
    assert isinstance(result, (int, float))

@given(st.lists(st.integers(), min_size=1))
def test_median_odd_length_property(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        mid_index = len(sorted_data) // 2
        result = statistics.median(sorted_data)
        assert result == sorted_data[mid_index]

@given(st.lists(st.integers(), min_size=2))
def test_median_even_length_property(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        mid_index1 = len(sorted_data) // 2 - 1
        mid_index2 = len(sorted_data) // 2
        expected_result = (sorted_data[mid_index1] + sorted_data[mid_index2]) / 2
        result = statistics.median(sorted_data)
        assert result == expected_result

@given(st.lists(st.integers()))
def test_median_sorted_property(data):
    sorted_data = sorted(data)
    result_unsorted = statistics.median(data)
    result_sorted = statistics.median(sorted_data)
    assert result_unsorted == result_sorted

@given(st.lists(st.integers(), min_size=0))
def test_median_empty_list_property(data):
    if len(data) == 0:
        try:
            statistics.median(data)
            assert False  # Should raise an exception
        except StatisticsError:
            assert True  # Correct behavior