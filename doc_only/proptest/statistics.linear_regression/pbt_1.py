from hypothesis import given, strategies as st
import statistics
import math

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_slope_is_finite_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Check for valid input
        slope, intercept = statistics.linear_regression(x, y)
        assert math.isfinite(slope)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_intercept_is_finite_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Check for valid input
        slope, intercept = statistics.linear_regression(x, y)
        assert math.isfinite(intercept)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_intercept_zero_when_proportional_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Check for valid input
        slope, intercept = statistics.linear_regression(x, y, proportional=True)
        assert intercept == 0.0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_slope_changes_predictably_property(x, y):
    if len(x) == len(y) and len(set(x)) > 1:  # Check for valid input
        original_slope, _ = statistics.linear_regression(x, y)
        scaled_x = [value * 2 for value in x]  # Scale x values
        scaled_slope, _ = statistics.linear_regression(scaled_x, y)
        assert scaled_slope == original_slope * 2  # Slope should scale by the same factor

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_statistics_error_on_invalid_inputs_property(x, y):
    if len(x) != len(y) or len(set(x)) <= 1:  # Invalid input cases
        try:
            statistics.linear_regression(x, y)
            assert False  # If no exception, the test fails
        except statistics.StatisticsError:
            assert True  # If exception is raised, the test passes
# End program