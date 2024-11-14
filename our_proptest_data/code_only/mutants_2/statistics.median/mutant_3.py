# property to violate: The median of a list with an odd number of elements is the middle element of the sorted list.
from hypothesis import given, strategies as st
from statistics import median

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_1(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return the first element instead of the middle element
        assert median(sorted_data) == sorted_data[0]

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_2(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return the last element instead of the middle element
        assert median(sorted_data) == sorted_data[-1]

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_3(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return the second element instead of the middle element
        assert median(sorted_data) == sorted_data[1]

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_4(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return the middle element plus one instead of the middle element
        assert median(sorted_data) == sorted_data[len(sorted_data) // 2] + 1

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_5(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 1:
        # Return the middle element minus one instead of the middle element
        assert median(sorted_data) == sorted_data[len(sorted_data) // 2] - 1