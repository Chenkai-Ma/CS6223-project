from hypothesis import given, strategies as st
from statistics import mean, StatisticsError
from fractions import Fraction
from decimal import Decimal

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_non_empty_numeric_property(data):
    result = mean(data)
    assert isinstance(result, (float, Decimal, Fraction))

@given(st.lists(st.just(5.0), min_size=1))
def test_mean_identical_values_property(data):
    result = mean(data)
    assert result == 5.0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1),
       st.floats(allow_nan=False, allow_infinity=False))
def test_mean_outlier_effect_property(data, outlier):
    original_mean = mean(data)
    modified_data = data + [outlier]
    modified_mean = mean(modified_data)
    assert modified_mean != original_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_mean_empty_dataset_property(data):
    if len(data) == 0:
        try:
            mean(data)
            assert False  # Should not reach here
        except StatisticsError:
            pass  # Expected behavior

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_add_zero_invariance_property(data):
    original_mean = mean(data)
    modified_mean = mean(data + [0])
    assert original_mean == modified_mean
# End program