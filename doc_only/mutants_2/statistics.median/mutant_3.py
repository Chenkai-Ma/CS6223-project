# property to violate: If the input list has an even number of elements, the median should be the average of the two middle elements when the list is sorted.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_1(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2 + 1  # Adding 1 to violate the property

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_2(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2 - 1  # Subtracting 1 to violate the property

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_3(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2 * 2  # Doubling the median to violate the property

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_4(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2 / 2  # Halving the median to violate the property

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_violation_of_statistics_median_5(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2 + sorted_data[len(sorted_data) // 2]  # Adding an extra middle element to violate the property