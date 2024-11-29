from hypothesis import given, strategies as st
from statistics import linear_regression, StatisticsError, LinearRegression
import numpy as np

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2), 
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_slope_zero_when_y_constant_property(xs, ys):
    constant_value = ys[0]
    ys = [constant_value] * len(xs)
    result = linear_regression(xs, ys)
    assert result.slope == 0.0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2),
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_intercept_equals_mean_y_when_slope_zero_property(xs, ys):
    constant_value = ys[0]
    ys = [constant_value] * len(xs)
    result = linear_regression(xs, ys, proportional=False)
    assert result.intercept == np.mean(ys)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2), 
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_output_is_linear_regression_object_property(xs, ys):
    result = linear_regression(xs, ys)
    assert isinstance(result, LinearRegression)
    assert isinstance(result.slope, float)
    assert isinstance(result.intercept, float)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2), 
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_slope_changes_continuously_property(xs, ys):
    result1 = linear_regression(xs, ys)
    ys[0] += 1  # Modify ys to create a different linear relationship
    result2 = linear_regression(xs, ys)
    assert result1.slope != result2.slope

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1), 
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_statistics_error_with_less_than_two_points_property(xs, ys):
    if len(xs) < 2 or len(ys) < 2:
        try:
            linear_regression(xs, ys)
            assert False  # Should have raised an error
        except StatisticsError:
            assert True  # The error was raised as expected
# End program