from hypothesis import given, strategies as st
from statistics import median, StatisticsError

@given(st.lists(st.integers(), max_size=1000))  # Test with lists of integers up to size 1000
def test_median_middle_value_property(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        assert median(data) == sorted_data[len(sorted_data) // 2]

@given(st.lists(st.integers(), min_size=2, max_size=1000))  # Test with lists of integers of even size
def test_median_average_of_middle_values_property(data):
    sorted_data = sorted(data)
    assert median(data) == (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2

@given(st.lists(st.integers(), max_size=1000))  # Test with lists of integers
def test_median_empty_data_property(data):
    if len(data) == 0:
        try:
            median(data)
            assert False  # Should not reach here
        except StatisticsError:
            assert True  # Expected exception raised

@given(st.lists(st.integers(), max_size=1000))  # Test with lists of integers
def test_median_robustness_against_outliers_property(data):
    outlier_data = data + [max(data) + 1]  # Adding an outlier
    regular_median = median(data)
    outlier_median = median(outlier_data)
    assert outlier_median != (regular_median + 1)  # Outlier shouldn't affect median significantly

@given(st.lists(st.integers(), max_size=1000))  # Test with lists of integers
def test_median_order_independence_property(data):
    sorted_data = sorted(data)
    assert median(data) == median(sorted_data)

# End program