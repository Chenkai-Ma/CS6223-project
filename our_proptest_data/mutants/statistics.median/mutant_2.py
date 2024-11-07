# property to violate: If the input list has an odd number of elements, the median should be equal to the middle element when the list is sorted.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_1(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result != sorted_data[len(sorted_data) // 2]  # Change to not equal

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_2(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == sorted_data[len(sorted_data) // 2] + 1  # Add 1 to the median

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_3(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == sorted_data[len(sorted_data) // 2] - 1  # Subtract 1 from the median

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_4(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == 0  # Force the median to be 0, which is incorrect

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_5(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == sorted_data[len(sorted_data) // 2] * 2  # Double the median