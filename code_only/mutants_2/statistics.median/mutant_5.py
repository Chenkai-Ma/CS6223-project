# property to violate: The median is invariant under the order of the input data; that is, sorting the data before finding the median should yield the same result as finding the median directly from the unsorted data.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_1(data):
    sorted_data = sorted(data)
    # Intentionally return an incorrect median value by adding 1 to the median of the unsorted data
    assert statistics.median(data) + 1 == statistics.median(sorted_data)

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_2(data):
    sorted_data = sorted(data)
    # Intentionally return an incorrect median value by subtracting 1 from the median of the unsorted data
    assert statistics.median(data) - 1 == statistics.median(sorted_data)

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_3(data):
    sorted_data = sorted(data)
    # Intentionally return a completely different value (e.g., 0) instead of the median
    assert 0 == statistics.median(sorted_data)

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_4(data):
    sorted_data = sorted(data)
    # Intentionally return a value that is always greater than the median of the sorted data
    assert statistics.median(data) + 10 == statistics.median(sorted_data)

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_5(data):
    sorted_data = sorted(data)
    # Intentionally return a value that is always less than the median of the sorted data
    assert statistics.median(data) - 10 == statistics.median(sorted_data)