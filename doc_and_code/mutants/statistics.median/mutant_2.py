# property to violate: The output is the average of the two middle values of the sorted input data when the number of elements is even.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_1(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2
        # Violate the property by returning the sum of the two middle values instead of their average
        assert statistics.median(data) == (sorted_data[i - 1] + sorted_data[i])

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_2(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2
        # Violate the property by returning the first middle value instead of the average
        assert statistics.median(data) == sorted_data[i - 1]

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_3(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2
        # Violate the property by returning the second middle value instead of the average
        assert statistics.median(data) == sorted_data[i]

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_4(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2
        # Violate the property by returning a fixed number instead of the average
        assert statistics.median(data) == 0  # Arbitrary fixed number

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_5(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2
        # Violate the property by returning the average of the entire list instead of the middle values' average
        assert statistics.median(data) == sum(sorted_data) / n