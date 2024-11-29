from hypothesis import given, strategies as st
import statistics
from statistics import StatisticsError
from fractions import Fraction as F
from decimal import Decimal as D


@given(st.lists(st.floats(), min_size=1))
def test_mean_non_empty_numeric_output_property(data):
    result = statistics.mean(data)
    assert isinstance(result, (float, int, Decimal, F))


@given(st.lists(st.integers(), min_size=1))
def test_mean_identical_values_property(data):
    identical_value = data[0]
    identical_data = [identical_value] * len(data)
    result = statistics.mean(identical_data)
    assert result == identical_value


@given(st.lists(st.floats(), min_size=1), st.floats())
def test_mean_outlier_impact_property(data, outlier):
    original_mean = statistics.mean(data)
    modified_data = data + [outlier]
    modified_mean = statistics.mean(modified_data)
    assert modified_mean != original_mean


@given(st.lists(st.floats(), min_size=0))
def test_mean_empty_data_statistics_error_property(data):
    if len(data) == 0:
        try:
            statistics.mean(data)
            assert False, "Expected StatisticsError for empty data"
        except StatisticsError:
            pass  # Expected behavior
    else:
        statistics.mean(data)  # Should not raise an error


@given(st.lists(st.floats(), min_size=1))
def test_mean_invariance_under_addition_of_zero_property(data):
    original_mean = statistics.mean(data)
    modified_data = data + [0]
    modified_mean = statistics.mean(modified_data)
    assert modified_mean == original_mean

# End program