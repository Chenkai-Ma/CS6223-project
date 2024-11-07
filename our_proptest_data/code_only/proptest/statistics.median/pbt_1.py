from hypothesis import given, strategies as st
from statistics import median, StatisticsError

@given(st.lists(st.integers(min_value=-1e9, max_value=1e9)))
def test_median_of_empty_list_property(data):
    if len(data) == 0:
        with pytest.raises(StatisticsError):
            median(data)
# End program

@given(st.integers(min_value=-1e9, max_value=1e9))
def test_median_of_single_element_list_property(value):
    assert median([value]) == value
# End program

@given(st.lists(st.integers(min_value=-1e9, max_value=1e9), min_size=1))
def test_median_of_odd_number_of_elements_property(data):
    if len(data) % 2 == 1:
        assert median(data) == median(sorted(data))
# End program

@given(st.lists(st.integers(min_value=-1e9, max_value=1e9), min_size=2))
def test_median_of_even_number_of_elements_property(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        expected_median = (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2
        assert median(data) == expected_median
# End program

@given(st.lists(st.integers(min_value=-1e9, max_value=1e9)))
def test_invariance_under_order_property(data):
    assert median(data) == median(sorted(data))
# End program