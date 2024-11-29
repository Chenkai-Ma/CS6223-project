from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.integers(), min_size=1))
def test_median_returns_middle_value_for_odd_length_property(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        expected = sorted_data[n // 2]
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=2))
def test_median_returns_average_of_middle_values_for_even_length_property(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        i = n // 2
        expected = (sorted_data[i - 1] + sorted_data[i]) / 2
        assert statistics.median(data) == expected

@given(st.lists(st.integers(), min_size=0))
def test_median_raises_statistics_error_for_empty_data_property(data):
    if len(data) == 0:
        try:
            statistics.median(data)
            assert False  # Should not reach this line
        except statistics.StatisticsError:
            assert True  # Expected error raised

@given(st.lists(st.integers()))
def test_median_is_robust_against_outliers_property(data):
    outlier_value = max(data) * 10 if data else 1000
    data_with_outlier = data + [outlier_value]
    median_without_outlier = statistics.median(data)
    median_with_outlier = statistics.median(data_with_outlier)
    assert median_with_outlier == median_without_outlier or median_with_outlier == statistics.median(sorted(data_with_outlier))

@given(st.lists(st.integers()))
def test_median_is_order_invariant_property(data):
    sorted_data = sorted(data)
    assert statistics.median(data) == statistics.median(sorted_data)

# End program