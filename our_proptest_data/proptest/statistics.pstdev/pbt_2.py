from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_statistics_pstdev_non_negative_property(data):
    result = statistics.pstdev(data)
    assert result >= 0
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_statistics_pstdev_constant_list_property(data):
    if len(data) > 0:
        constant_value = data[0]
        constant_list = [constant_value] * len(data)
        result = statistics.pstdev(constant_list)
        assert result == 0
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_statistics_pstdev_increasing_variability_property(data):
    if len(data) > 1:
        original_variance = statistics.pstdev(data)
        expanded_data = data + [max(data) + 10]  # Adding an outlier to increase variability
        result = statistics.pstdev(expanded_data)
        assert result >= original_variance
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_statistics_pstdev_same_variance_property(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = statistics.pstdev(modified_data)
        assert result_original == result_modified
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_statistics_pstdev_equivalence_with_pvariance_property(data):
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev == result_pvariance
# End program