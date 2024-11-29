from hypothesis import given, strategies as st
from statistics import linear_regression, StatisticsError, LinearRegression

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1), st.lists(st.floats(), min_size=2))
def test_slope_zero_when_y_constant_property(x, y):
    # Ensure all y values are the same (constant)
    constant_y = [y[0]] * len(y)
    result = linear_regression(x, constant_y)
    assert result.slope == 0.0

@given(st.lists(st.floats(), min_size=2), st.lists(st.floats(), min_size=2))
def test_intercept_equals_mean_when_slope_zero_property(x, y):
    # Ensure that the slope is zero
    constant_y = [y[0]] * len(y)
    result = linear_regression(x, constant_y)
    assert result.intercept == sum(constant_y) / len(constant_y)

@given(st.lists(st.floats(), min_size=2), st.lists(st.floats(), min_size=2))
def test_output_is_linear_regression_object_property(x, y):
    result = linear_regression(x, y)
    assert isinstance(result, LinearRegression)
    assert isinstance(result.slope, float)
    assert isinstance(result.intercept, float)

@given(st.lists(st.floats(), min_size=2), st.lists(st.floats(), min_size=2))
def test_slope_changes_continuously_property(x, y):
    # Generate pairs of lists with slight variations
    result1 = linear_regression(x, y)
    perturbed_y = [yi + 0.1 for yi in y]
    result2 = linear_regression(x, perturbed_y)
    assert result1.slope != result2.slope

@given(st.lists(st.floats(), min_size=1))
def test_statistics_error_when_n_less_than_two_property(x):
    if len(x) < 2:
        try:
            linear_regression(x, x)
            assert False, "Should have raised StatisticsError"
        except StatisticsError:
            pass  # Expected behavior