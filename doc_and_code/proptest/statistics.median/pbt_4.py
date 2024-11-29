from hypothesis import given, strategies as st
from statistics import median, StatisticsError

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_median_middle_value_property(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    expected_output = sorted_data[n // 2] if n % 2 == 1 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    assert median(data) == expected_output

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_median_average_of_middle_values_property(data):
    if len(data) == 0:
        try:
            median(data)
            assert False  # should raise exception
        except StatisticsError:
            pass
    else:
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            expected_output = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
            assert median(data) == expected_output

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_median_empty_data_property(data):
    if len(data) == 0:
        try:
            median(data)
            assert False  # should raise exception
        except StatisticsError:
            pass

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_median_outlier_robustness_property(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return  # Skip empty lists
    mean_value = sum(sorted_data) / n
    median_value = median(data)
    assert abs(median_value - mean_value) <= abs(median_value - mean(sorted_data))  # Median should be less affected by outliers

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_median_order_independence_property(data):
    assert median(data) == median(sorted(data))

# End program