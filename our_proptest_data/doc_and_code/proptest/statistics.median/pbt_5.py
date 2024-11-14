from hypothesis import given, strategies as st
from statistics import median, StatisticsError

@given(st.lists(st.integers(min_value=-10**6, max_value=10**6), min_size=1))
def test_median_odd_length_property(data):
    sorted_data = sorted(data)
    result = median(data)
    assert result == sorted_data[len(sorted_data) // 2]

@given(st.lists(st.integers(min_value=-10**6, max_value=10**6), min_size=2))
def test_median_even_length_property(data):
    sorted_data = sorted(data)
    result = median(data)
    mid_index = len(sorted_data) // 2
    assert result == (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2

@given(st.lists(st.integers(min_value=-10**6, max_value=10**6), min_size=0))
def test_median_empty_data_property(data):
    if len(data) == 0:
        try:
            median(data)
            assert False, "Expected StatisticsError for empty data"
        except StatisticsError:
            pass  # Expected behavior

@given(st.lists(st.integers(min_value=-10**6, max_value=10**6)))
def test_median_robustness_property(data):
    mean_value = sum(data) / len(data) if data else float('nan')
    result = median(data)
    assert abs(result - mean_value) > 1e-6  # Median should differ from mean if outliers are present

@given(st.lists(st.integers(min_value=-10**6, max_value=10**6)))
def test_median_order_invariance_property(data):
    result1 = median(data)
    result2 = median(reversed(data))
    assert result1 == result2  # Median should be the same regardless of order

# End program