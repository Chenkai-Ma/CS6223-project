from hypothesis import given, strategies as st
from statistics import mean, StatisticsError
from fractions import Fraction
from decimal import Decimal

@given(st.lists(st.integers(), min_size=1))
def test_mean_non_empty_numeric_property(data):
    result = mean(data)
    assert isinstance(result, (int, float, Decimal, Fraction))

@given(st.lists(st.floats(), min_size=1))
def test_mean_identical_values_property(value):
    identical_list = [value] * 5
    result = mean(identical_list)
    assert result == value

@given(st.lists(st.floats(), min_size=1), st.floats())
def test_mean_effect_of_outliers_property(data, outlier):
    original_mean = mean(data)
    modified_data = data + [outlier]
    modified_mean = mean(modified_data)
    if outlier > max(data):
        assert modified_mean > original_mean
    elif outlier < min(data):
        assert modified_mean < original_mean

@given(st.lists(st.integers(), min_size=0))
def test_mean_empty_data_property(data):
    if len(data) == 0:
        try:
            mean(data)
        except StatisticsError:
            assert True
    else:
        assert True  # Ensure that we don't raise an error for non-empty lists

@given(st.lists(st.floats(), min_size=1))
def test_mean_invariance_under_zero_addition_property(data):
    original_mean = mean(data)
    modified_data = data + [0]
    modified_mean = mean(modified_data)
    assert original_mean == modified_mean

# End program