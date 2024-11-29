from hypothesis import given, strategies as st
import statistics
import math

@given(st.lists(st.floats(), min_size=2, max_size=100), st.lists(st.floats(), min_size=2, max_size=100))
def test_slope_is_finite_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Ensure x is not constant
        slope, _ = statistics.linear_regression(x, y)
        assert math.isfinite(slope)

@given(st.lists(st.floats(), min_size=2, max_size=100), st.lists(st.floats(), min_size=2, max_size=100))
def test_intercept_is_finite_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Ensure x is not constant
        _, intercept = statistics.linear_regression(x, y)
        assert math.isfinite(intercept)

@given(st.lists(st.floats(), min_size=2, max_size=100), st.lists(st.floats(), min_size=2, max_size=100))
def test_intercept_zero_when_proportional_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Ensure x is not constant
        slope, intercept = statistics.linear_regression(x, y, proportional=True)
        assert intercept == 0.0

@given(st.lists(st.floats(), min_size=2, max_size=100), st.lists(st.floats(), min_size=2, max_size=100))
def test_slope_predictable_change_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Ensure x is not constant
        original_slope, _ = statistics.linear_regression(x, y)
        scaled_x = [value * 2 for value in x]
        scaled_slope, _ = statistics.linear_regression(scaled_x, y)
        assert scaled_slope == 2 * original_slope  # Scaling x should double the slope

@given(st.lists(st.floats(), min_size=2, max_size=100), st.lists(st.floats(), min_size=2, max_size=100))
def test_statistics_error_on_constant_x_property(x, y):
    if len(set(x)) == 1 or len(x) != len(y):
        try:
            statistics.linear_regression(x, y)
        except statistics.StatisticsError:
            assert True
        else:
            assert False
# End program