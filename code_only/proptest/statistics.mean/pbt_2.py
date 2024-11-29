from hypothesis import given, strategies as st
from statistics import mean, StatisticsError

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_identical_elements_property(data):
    if len(data) > 0:
        identical_value = data[0]
        assert mean([identical_value] * len(data)) == identical_value

@given()
def test_mean_empty_list_property():
    with st.raises(StatisticsError):
        mean([])

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_mean_range_property(data):
    if data:
        calculated_mean = mean(data)
        assert min(data) <= calculated_mean <= max(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_zero_addition_property(data):
    calculated_mean = mean(data)
    assert mean(data + [0]) == calculated_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_mean_concat_weighted_average_property(list1, list2):
    if list1 and list2:
        mean1 = mean(list1)
        mean2 = mean(list2)
        combined_list = list1 + list2
        calculated_mean = mean(combined_list)
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean
# End program