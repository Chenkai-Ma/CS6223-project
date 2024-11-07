from hypothesis import given, strategies as st
from statistics import median, StatisticsError

@given(st.lists(st.integers(), min_size=0))
def test_median_empty_list_property(data):
    if len(data) == 0:
        with pytest.raises(StatisticsError):
            median(data)
    # End program

@given(st.integers())
def test_median_single_element_list_property(x):
    assert median([x]) == x
    # End program

@given(st.lists(st.integers(), min_size=1))
def test_median_odd_length_list_property(data):
    if len(data) % 2 == 1:
        result = median(data)
        sorted_data = sorted(data)
        assert result == sorted_data[len(sorted_data) // 2]
    # End program

@given(st.lists(st.integers(), min_size=2))
def test_median_even_length_list_property(data):
    if len(data) % 2 == 0:
        result = median(data)
        sorted_data = sorted(data)
        mid_index = len(sorted_data) // 2
        expected_result = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
        assert result == expected_result
    # End program

@given(st.lists(st.integers(), min_size=1))
def test_median_order_invariance_property(data):
    sorted_data = sorted(data)
    assert median(data) == median(sorted_data)
    # End program