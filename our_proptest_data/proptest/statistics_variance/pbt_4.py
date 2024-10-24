from hypothesis import given, strategies as st
from statistics import variance, StatisticsError

@given(st.lists(st.floats(), min_size=2))
def test_output_non_negative_property(data):
    result = variance(data)
    assert result >= 0

@given(st.lists(st.floats(), min_size=2))
def test_identical_values_zero_variance_property(data):
    if len(set(data)) == 1:  # All values are identical
        result = variance(data)
        assert result == 0

@given(st.lists(st.floats(), min_size=2))
def test_increased_spread_increases_variance_property(data):
    if len(data) > 0:
        mean_original = sum(data) / len(data)
        spread_original = max(data) - min(data)
        
        # Increase spread by adding a constant
        increased_data = [x + spread_original for x in data]
        result_original = variance(data)
        result_increased = variance(increased_data)
        
        assert result_increased >= result_original

@given(st.lists(st.floats(), min_size=2), st.floats())
def test_constant_addition_invariance_property(data, constant):
    adjusted_data = [x + constant for x in data]
    result_original = variance(data)
    result_adjusted = variance(adjusted_data)
    
    assert result_original == result_adjusted

@given(st.lists(st.floats(), min_size=2))
def test_mean_passed_as_xbar_property(data):
    mean_value = sum(data) / len(data)
    result_default = variance(data)
    result_with_xbar = variance(data, mean_value)
    
    assert result_default == result_with_xbar
# End program