from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=100))
def test_statistics_pstdev_non_negative_property(data):
    result = statistics.pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=100))
def test_statistics_pstdev_constant_list_property(data):
    if len(set(data)) == 1:  # All elements are the same
        result = statistics.pstdev(data)
        assert result == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=100))
def test_statistics_pstdev_variability_increases_property(data):
    if len(data) > 1:
        result1 = statistics.pstdev(data)
        result2 = statistics.pstdev(data + [max(data) + 1])  # Adding a value to increase variability
        assert result2 >= result1

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=100))
def test_statistics_pstdev_modify_variance_property(data):
    if len(data) > 1:
        result1 = statistics.pstdev(data)
        modified_data = [x + 3 for x in data]  # Adding a constant to all elements
        result2 = statistics.pstdev(modified_data)
        assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=100))
def test_statistics_pstdev_equivalence_with_pvariance_property(data):
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data) ** 0.5  # Square root of pvariance
    assert result_pstdev == result_pvariance
# End program