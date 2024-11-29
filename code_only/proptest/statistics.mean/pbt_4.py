from hypothesis import given, strategies as st
from statistics import mean, StatisticsError

@given(st.lists(st.floats()))
def test_mean_identical_elements_property(data):
    if data:  # Ensure there are elements to test
        identical_value = data[0]
        identical_list = [identical_value] * len(data)
        assert mean(identical_list) == identical_value

@given()
def test_mean_empty_list_property():
    with st.raises(StatisticsError):
        mean([])

@given(st.lists(st.floats()))
def test_mean_range_property(data):
    if data:  # Ensure there are elements to test
        calculated_mean = mean(data)
        assert min(data) <= calculated_mean <= max(data)

@given(st.lists(st.floats()))
def test_mean_invariance_under_zero_property(data):
    zero_added_data = data + [0]
    assert mean(data) == mean(zero_added_data)

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_mean_concat_lists_property(data1, data2):
    if data1 and data2:  # Ensure both lists have elements to test
        mean1 = mean(data1)
        mean2 = mean(data2)
        combined_list = data1 + data2
        combined_mean = mean(combined_list)
        assert combined_mean == (mean1 * len(data1) + mean2 * len(data2)) / (len(data1) + len(data2))
# End program