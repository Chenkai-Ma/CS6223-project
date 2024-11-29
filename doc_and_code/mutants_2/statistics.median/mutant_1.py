# property to violate: The output is the middle value of the sorted input data when the number of elements is odd.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_1(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        expected = sorted_data[n // 2] + 1  # Adding 1 to the expected value to violate the property
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_2(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        expected = sorted_data[n // 2] - 1  # Subtracting 1 from the expected value to violate the property
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_3(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        expected = sorted_data[n // 2] * 2  # Multiplying the expected value by 2 to violate the property
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_4(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        expected = sorted_data[n // 2] / 2  # Dividing the expected value by 2 to violate the property
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=1))
def test_violation_of_statistics_median_5(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        expected = -sorted_data[n // 2]  # Negating the expected value to violate the property
        assert statistics.median(data) == expected