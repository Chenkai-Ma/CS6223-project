from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_statistics_pstdev_non_negative_property(data):
    result = statistics.pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_statistics_pstdev_constant_list_property(data):
    constant_data = [data[0]] * len(data)
    result = statistics.pstdev(constant_data)
    assert result == 0

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=1, max_size=1000))
def test_statistics_pstdev_increase_with_variability_property(data):
    varied_data = data + [data[0] + 10]  # Adding a value to increase variability
    result_original = statistics.pstdev(data)
    result_varied = statistics.pstdev(varied_data)
    assert result_varied >= result_original

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_statistics_pstdev_no_change_with_constant_addition_property(data):
    modified_data = [x + 5 for x in data]  # Adding a constant to all elements
    result_original = statistics.pstdev(data)
    result_modified = statistics.pstdev(modified_data)
    assert result_original == result_modified

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_statistics_pstdev_square_root_of_variance_property(data):
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data)
    assert result_pstdev == result_pvariance ** 0.5
# End program