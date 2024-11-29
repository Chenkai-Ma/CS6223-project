# property to violate: If the input list has an odd number of elements, the median should be equal to the middle element when the list is sorted.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_1(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Modify the result to be something other than the middle element
        assert result != sorted_data[len(sorted_data) // 2]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_2(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Change the result to be the first element of the sorted list
        assert result != sorted_data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_3(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Change the result to be the last element of the sorted list
        assert result != sorted_data[-1]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_4(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Modify the result to be a value that is not in the sorted list
        assert result != sorted_data[len(sorted_data) // 2] + 1

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_median_5(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Change the result to be the average of the first and last elements
        assert result != (sorted_data[0] + sorted_data[-1]) / 2