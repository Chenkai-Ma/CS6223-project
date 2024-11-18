# property to violate: The output should remain the same if the input list is modified by adding or removing elements that do not change the overall variance (e.g., adding a constant value to all elements).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_1(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = statistics.pstdev(modified_data) + 1  # Violate the property by adding 1
        assert result_original == result_modified

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_2(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = statistics.pstdev(modified_data) * 2  # Violate the property by multiplying by 2
        assert result_original == result_modified

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_3(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = statistics.pstdev(modified_data) - 3  # Violate the property by subtracting 3
        assert result_original == result_modified

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_4(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = statistics.pstdev(modified_data) + statistics.pstdev(data)  # Violate by adding original result
        assert result_original == result_modified

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_5(data):
    if len(data) > 0:
        constant_value = 5.0
        modified_data = [x + constant_value for x in data]
        result_original = statistics.pstdev(data)
        result_modified = statistics.pstdev(modified_data) ** 2  # Violate the property by squaring the result
        assert result_original == result_modified