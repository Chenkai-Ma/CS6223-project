from hypothesis import given, strategies as st
import statistics
from fractions import Fraction
from decimal import Decimal
from hypothesis import HealthCheck, settings

# Setting health check to ignore certain issues due to large inputs
settings.register_profile("ignore_large", max_examples=100, suppress_health_check=[HealthCheck.data_too_large])
settings.set_profile("ignore_large")

@given(st.lists(st.floats(), min_size=1))
def test_mean_numeric_output_property(data):
    result = statistics.mean(data)
    assert isinstance(result, (float, Decimal, Fraction)), "Mean should be a numeric type"

@given(st.lists(st.floats()))
def test_mean_identical_values_property(data):
    if len(data) > 0:
        identical_value = data[0]
        mean_value = statistics.mean([identical_value] * len(data))
        assert mean_value == identical_value, "Mean of identical values should equal that value"

@given(st.lists(st.floats(), min_size=1), st.floats())
def test_mean_outlier_effect_property(data, outlier):
    original_mean = statistics.mean(data)
    altered_data = data + [outlier]
    altered_mean = statistics.mean(altered_data)
    assert (outlier > original_mean and altered_mean > original_mean) or \
           (outlier < original_mean and altered_mean < original_mean), "Mean should be affected by outliers"

@given(st.lists(st.floats()))
def test_mean_empty_data_property(data):
    if len(data) == 0:
        try:
            statistics.mean(data)
            assert False, "Mean should raise StatisticsError for empty data"
        except statistics.StatisticsError:
            pass  # Expected behavior

@given(st.lists(st.floats(), min_size=1))
def test_mean_invariance_under_zero_property(data):
    original_mean = statistics.mean(data)
    mean_with_zero = statistics.mean(data + [0])
    assert mean_with_zero == original_mean, "Mean should be invariant under the addition of zero"
# End program