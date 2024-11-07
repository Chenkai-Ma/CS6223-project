from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats()))
def test_statistics_pstdev_non_negative_property(data):
    result = statistics.pstdev(data)
    assert result >= 0
# End program

@given(st.lists(st.floats(min_value=1.0, max_value=1.0), min_size=1, max_size=5))
def test_statistics_pstdev_constant_list_property(data):
    result = statistics.pstdev(data)
    assert result == 0
# End program

@given(st.lists(st.floats(), min_size=2))
def test_statistics_pstdev_increasing_variability_property(data):
    original_variance = statistics.pstdev(data)
    expanded_data = data + [max(data) + 1]  # Adding a value to increase variability
    new_variance = statistics.pstdev(expanded_data)
    assert new_variance >= original_variance
# End program

@given(st.lists(st.floats(), min_size=1))
def test_statistics_pstdev_constant_shift_property(data):
    constant_shift = 5.0
    result_original = statistics.pstdev(data)
    result_shifted = statistics.pstdev([x + constant_shift for x in data])
    assert result_original == result_shifted
# End program

@given(st.lists(st.floats()))
def test_statistics_pstdev_equivalence_with_pvariance_property(data):
    if len(data) > 1:  # pvariance requires at least two elements
        result_pstdev = statistics.pstdev(data)
        result_pvariance = statistics.pvariance(data) ** 0.5
        assert result_pstdev == result_pvariance
# End program