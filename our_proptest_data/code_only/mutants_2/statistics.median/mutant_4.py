# property to violate: The median of a list with an even number of elements is the average of the two middle elements of the sorted list.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_1(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 0:
        mid_index = len(sorted_data) // 2
        expected_median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2 + 1  # Adding 1 to violate the property
        assert statistics.median(sorted_data) == expected_median

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_2(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 0:
        mid_index = len(sorted_data) // 2
        expected_median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2 - 1  # Subtracting 1 to violate the property
        assert statistics.median(sorted_data) == expected_median

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_3(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 0:
        mid_index = len(sorted_data) // 2
        expected_median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2 * 2  # Multiplying by 2 to violate the property
        assert statistics.median(sorted_data) == expected_median

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_4(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 0:
        mid_index = len(sorted_data) // 2
        expected_median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2 / 2  # Dividing by 2 to violate the property
        assert statistics.median(sorted_data) == expected_median

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_5(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 0:
        mid_index = len(sorted_data) // 2
        expected_median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2 + sorted_data[mid_index - 1]  # Adding one of the middle elements to violate the property
        assert statistics.median(sorted_data) == expected_median