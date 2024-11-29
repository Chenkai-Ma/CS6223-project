from hypothesis import given, strategies as st
from statistics import linear_regression, StatisticsError, LinearRegression
import numpy as np

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_slope_zero_when_y_constant_property(xs, ys):
    # If all y values are constant, the slope should be zero
    y_constant = [ys[0]] * len(xs)
    result = linear_regression(xs, y_constant)
    assert result.slope == 0.0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_intercept_equals_mean_when_proportional_zero_slope_property(xs, ys):
    # If inputs have the same y value, the intercept should equal the mean of y when proportional is False
    y_constant = [ys[0]] * len(xs)
    result = linear_regression(xs, y_constant, proportional=False)
    assert result.intercept == np.mean(y_constant)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_output_is_valid_LinearRegression_object_property(xs, ys):
    # The output should be a valid LinearRegression object
    result = linear_regression(xs, ys)
    assert isinstance(result, LinearRegression)
    assert isinstance(result.slope, float)
    assert isinstance(result.intercept, float)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_slope_changes_continuously_property(xs, ys):
    # The slope should change as the input values change
    original_result = linear_regression(xs, ys)
    modified_xs = [x + 1 for x in xs]
    modified_result = linear_regression(modified_xs, ys)
    assert original_result.slope != modified_result.slope

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_statistics_error_when_n_less_than_2_property(xs):
    # The function should raise StatisticsError when n < 2
    if len(xs) < 2:
        try:
            linear_regression(xs, xs)
        except StatisticsError:
            pass  # Expected behavior
        else:
            assert False  # Should not reach here
# End program