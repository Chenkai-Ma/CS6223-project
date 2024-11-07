from hypothesis import given, strategies as st
from statistics import median, StatisticsError

@given(st.lists(st.integers(), min_size=0))
def test_empty_list_raises_statistics_error(data):
    if len(data) == 0:
        try:
            median(data)
            assert False, "Expected StatisticsError for empty data"
        except StatisticsError:
            pass

@given(st.integers())
def test_single_element_list_equals_element(x):
    assert median([x]) == x

@given(st.lists(st.integers(), min_size=1))
def test_odd_length_list_returns_middle_element(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        assert median(sorted_data) == sorted_data[len(sorted_data) // 2]

@given(st.lists(st.integers(), min_size=2))
def test_even_length_list_returns_average_of_middle_elements(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 0:
        mid_index = len(sorted_data) // 2
        expected_median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
        assert median(sorted_data) == expected_median

@given(st.lists(st.integers(), min_size=1))
def test_median_invariant_under_order(data):
    sorted_data = sorted(data)
    assert median(data) == median(sorted_data)
# End program