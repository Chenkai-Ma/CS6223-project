# property to violate: The median of a list with an odd number of elements is the middle element of the sorted list.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_1(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return an incorrect value (e.g., the first element instead of the middle)
        assert statistics.median(sorted_data) == sorted_data[0]

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_2(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return an incorrect value (e.g., the last element instead of the middle)
        assert statistics.median(sorted_data) == sorted_data[-1]

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_3(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return an incorrect value (e.g., the average of the first and last elements)
        assert statistics.median(sorted_data) == (sorted_data[0] + sorted_data[-1]) / 2

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_4(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return an incorrect value (e.g., the middle index plus one)
        assert statistics.median(sorted_data) == sorted_data[(len(sorted_data) // 2) + 1]

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_5(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return an incorrect value (e.g., a constant value)
        assert statistics.median(sorted_data) == 999  # Arbitrary constant