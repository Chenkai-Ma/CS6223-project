from hypothesis import given, strategies as st
from statistics import median, StatisticsError

@given(st.lists(st.integers()))
def test_empty_list_property(data):
    if len(data) == 0:
        with pytest.raises(StatisticsError):
            median(data)

@given(st.lists(st.integers()))
def test_single_element_property(data):
    if len(data) == 1:
        assert median(data) == data[0]

@given(st.lists(st.integers()))
def test_odd_length_list_property(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        assert median(data) == sorted_data[len(data) // 2]

@given(st.lists(st.integers()))
def test_even_length_list_property(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        mid_index = len(data) // 2
        assert median(data) == (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2

@given(st.lists(st.integers()))
def test_order_invariance_property(data):
    sorted_data = sorted(data)
    assert median(data) == median(sorted_data)
# End program