from hypothesis import given, strategies as st
from statistics import mean, StatisticsError
from fractions import Fraction
from decimal import Decimal

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_non_empty_output_type_property(data):
    result = mean(data)
    assert isinstance(result, (float, Decimal, Fraction))

@given(st.integers(), st.integers())
def test_mean_identical_values_property(value1, value2):
    result = mean([value1, value1, value1])
    assert result == value1

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1), st.floats())
def test_mean_outlier_impact_property(data, outlier):
    original_mean = mean(data)
    altered_data = data + [outlier]
    altered_mean = mean(altered_data)
    assert altered_mean != original_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_mean_empty_data_property(data):
    if len(data) == 0:
        try:
            mean(data)
            assert False  # Should not reach here
        except StatisticsError:
            assert True  # Expected exception raised

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_invariance_under_zero_property(data):
    original_mean = mean(data)
    mean_with_zero = mean(data + [0])
    assert mean_with_zero == original_mean

# End program