from hypothesis import given, strategies as st
from statistics import median, StatisticsError

@given(st.lists(st.integers(), min_size=0))
def test_empty_list_property(data):
    if len(data) == 0:
        with st.raises(StatisticsError):
            median(data)

@given(st.lists(st.integers(), min_size=1))
def test_single_element_list_property(data):
    assert median(data) == data[0]

@given(st.lists(st.integers(), min_size=1))
def test_odd_number_of_elements_property(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        assert median(sorted_data) == sorted_data[len(sorted_data) // 2]

@given(st.lists(st.integers(), min_size=2))
def test_even_number_of_elements_property(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 0:
        i = len(sorted_data) // 2
        assert median(sorted_data) == (sorted_data[i - 1] + sorted_data[i]) / 2

@given(st.lists(st.integers(), min_size=1))
def test_order_invariance_property(data):
    sorted_data = sorted(data)
    assert median(data) == median(sorted_data)
# End program