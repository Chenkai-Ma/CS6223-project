from hypothesis import given, strategies as st
from statistics import mean, StatisticsError

@given(st.lists(st.floats(), min_size=1))
def test_mean_identical_elements_property(data):
    if len(data) > 0:
        identical_value = data[0]
        assert mean([identical_value] * len(data)) == identical_value
# End program

@given(st.lists(st.floats(), max_size=100))
def test_mean_empty_list_property(data):
    if len(data) == 0:
        with st.raises(StatisticsError):
            mean(data)
# End program

@given(st.lists(st.floats(), min_size=1))
def test_mean_range_property(data):
    calculated_mean = mean(data)
    assert min(data) <= calculated_mean <= max(data)
# End program

@given(st.lists(st.floats(), min_size=1))
def test_mean_invariance_under_zero_property(data):
    original_mean = mean(data)
    assert mean(data + [0]) == original_mean
# End program

@given(st.lists(st.floats(), min_size=1), st.lists(st.floats(), min_size=1))
def test_mean_concatenated_lists_property(list1, list2):
    mean1 = mean(list1)
    mean2 = mean(list2)
    combined_mean = mean(list1 + list2)
    weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
    assert combined_mean == weighted_mean
# End program