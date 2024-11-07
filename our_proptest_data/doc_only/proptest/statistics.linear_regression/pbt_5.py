from hypothesis import given, strategies as st
import statistics
import math

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100), 
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_slope_is_finite_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Ensure valid input
        slope, _ = statistics.linear_regression(x, y)
        assert math.isfinite(slope)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100), 
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_intercept_is_finite_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Ensure valid input
        _, intercept = statistics.linear_regression(x, y)
        assert math.isfinite(intercept)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100), 
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_intercept_zero_when_proportional_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Ensure valid input
        slope, intercept = statistics.linear_regression(x, y, proportional=True)
        assert intercept == 0.0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100), 
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_slope_changes_with_scaling_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Ensure valid input
        original_slope, _ = statistics.linear_regression(x, y)
        scaled_x = [xi * 2 for xi in x]  # Scale x values
        scaled_slope, _ = statistics.linear_regression(scaled_x, y)
        assert scaled_slope == 2 * original_slope  # Slope should double

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100), 
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_statistics_error_when_constant_x_property(x, y):
    if len(set(x)) == 1:  # Ensure x is constant
        try:
            statistics.linear_regression(x, y)
            assert False  # Should raise an error
        except statistics.StatisticsError:
            pass  # Expected behavior

# End program