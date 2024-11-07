from hypothesis import given, strategies as st
from statistics import linear_regression, StatisticsError, LinearRegression

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2).filter(lambda x: len(set(x)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2).filter(lambda x: len(set(x)) > 1))
def test_slope_zero_for_constant_y_property(x, y):
    # All y values are constant
    constant_y = [y[0]] * len(y)
    result = linear_regression(x, constant_y)
    assert result.slope == 0.0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2),
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_intercept_equals_mean_y_property(x, y):
    result = linear_regression(x, y, proportional=True)
    assert result.intercept == sum(y) / len(y)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2),
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_output_valid_linear_regression_object_property(x, y):
    result = linear_regression(x, y)
    assert isinstance(result, LinearRegression)
    assert isinstance(result.slope, float)
    assert isinstance(result.intercept, float)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
               st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_slope_continuity_property(x, y):
    base_slope = linear_regression(x, y).slope
    modified_x = [xi + 1 for xi in x]  # Slightly modify x
    new_slope = linear_regression(modified_x, y).slope
    assert new_slope != base_slope  # Expect a change in slope

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_minimum_data_points_property(x):
    if len(x) < 2:
        with pytest.raises(StatisticsError):
            linear_regression(x, x)
    else:
        linear_regression(x, x)  # Should not raise an error

# End program