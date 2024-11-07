# property to violate: If the input list has an even number of elements, the median should be the average of the two middle elements when the list is sorted.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_1(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Incorrectly return the first middle element instead of the average
        assert result == sorted_data[len(sorted_data) // 2 - 1]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_2(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Incorrectly return the second middle element instead of the average
        assert result == sorted_data[len(sorted_data) // 2]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_3(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Incorrectly return the average of the first and last element instead of the middle elements
        assert result == (sorted_data[0] + sorted_data[-1]) / 2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_4(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Incorrectly return a constant value instead of the average of the middle elements
        assert result == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_5(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        # Incorrectly return the sum of the two middle elements instead of the average
        assert result == sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]