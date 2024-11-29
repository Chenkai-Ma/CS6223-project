# property to violate: The output is the average of the two middle values of the sorted input data when the number of elements is even.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_1(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2 + 1  # Adding 1 to the expected value
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_2(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2 - 1  # Subtracting 1 from the expected value
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_3(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2 * 2  # Multiplying the expected value by 2
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_4(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2 / 2  # Dividing the expected value by 2
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=2))
def test_violation_of_statistics_median_5(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2 + (sorted_data[i - 1] - sorted_data[i])  # Adding the difference between middle values
        assert statistics.median(data) == expected