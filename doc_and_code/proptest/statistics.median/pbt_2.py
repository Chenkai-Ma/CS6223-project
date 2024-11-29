from hypothesis import given, strategies as st
from statistics import median, StatisticsError

@given(st.lists(st.integers(), max_size=1000))
def test_median_middle_value_property(data):
    if len(data) % 2 == 1:  # Odd length
        sorted_data = sorted(data)
        expected = sorted_data[len(data) // 2]
        assert median(data) == expected

@given(st.lists(st.integers(), min_size=2, max_size=1000))
def test_median_average_of_middle_values_property(data):
    if len(data) % 2 == 0:  # Even length
        sorted_data = sorted(data)
        expected = (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
        assert median(data) == expected

@given(st.lists(st.integers(), max_size=1000))
def test_median_empty_data_property(data):
    if len(data) == 0:
        try:
            median(data)
            assert False, "Expected StatisticsError for empty data"
        except StatisticsError:
            pass  # This is the expected outcome

@given(st.lists(st.integers(), max_size=1000))
def test_median_outlier_property(data):
    # The presence of outliers should not affect the median compared to the mean
    mean_value = sum(data) / len(data) if data else 0
    sorted_data = sorted(data)
    median_value = median(data)
    assert abs(median_value - mean_value) < 1e6  # Arbitrary large difference threshold

@given(st.lists(st.integers(), max_size=1000))
def test_median_order_invariance_property(data):
    assert median(data) == median(sorted(data))  # The median should be the same regardless of order
# End program