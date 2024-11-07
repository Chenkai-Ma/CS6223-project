# property to violate: The output should remain the same if the input list is modified by adding or removing elements that do not change the overall variance (e.g., adding a constant value to all elements).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_1(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = result_original + 1  # Violating the property by changing the result
        assert result_original == result_modified

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_2(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = result_original * 2  # Violating the property by doubling the result
        assert result_original == result_modified

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_3(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = result_original - 1  # Violating the property by subtracting from the result
        assert result_original == result_modified

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_4(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = result_original + 10  # Violating the property by adding 10 to the result
        assert result_original == result_modified

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_5(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = result_original / 2  # Violating the property by halving the result
        assert result_original == result_modified