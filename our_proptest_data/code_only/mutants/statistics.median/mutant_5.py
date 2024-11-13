# property to violate: The median is invariant under the order of the input data; that is, sorting the data before finding the median should yield the same result as finding the median directly from the unsorted data.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_1(data):
    sorted_data = sorted(data)
    assert median(data) != median(sorted_data)

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_2(data):
    sorted_data = sorted(data)
    assert median(data) != median(sorted_data) + 1

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_3(data):
    sorted_data = sorted(data)
    assert median(data) != median(sorted_data) - 1

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_4(data):
    sorted_data = sorted(data)
    assert median(data) != median(sorted_data) * 2

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_5(data):
    sorted_data = sorted(data)
    assert median(data) != median(sorted_data) / 2