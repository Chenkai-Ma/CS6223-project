from hypothesis import given, strategies as st
from statistics import linear_regression, StatisticsError
import numpy as np

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) > 1))
def test_slope_zero_when_y_constant_property(y_values):
    x_values = np.random.rand(len(y_values)).tolist()  # Random x values
    constant_y = [y_values[0]] * len(y_values)  # Make y constant
    result = linear_regression(x_values, constant_y)
    assert result.slope == 0.0

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) > 1))
def test_intercept_equals_mean_y_when_slope_zero_property(y_values):
    x_values = np.random.rand(len(y_values)).tolist()  # Random x values
    constant_y = [y_values[0]] * len(y_values)  # Make y constant
    result = linear_regression(x_values, constant_y, proportional=False)
    assert result.intercept == np.mean(constant_y)

@given(st.lists(st.floats(), min_size=2, max_size=100).filter(lambda lst: len(set(lst)) > 1),
                st.lists(st.floats(), min_size=2, max_size=100).filter(lambda lst: len(set(lst)) > 1)))
def test_output_is_valid_linear_regression_object_property(x_values, y_values):
    result = linear_regression(x_values, y_values)
    assert hasattr(result, 'slope')
    assert hasattr(result, 'intercept')
    assert isinstance(result.slope, float)
    assert isinstance(result.intercept, float)

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) > 1))
def test_slope_changes_continuously_property(y_values):
    x_values = np.random.rand(len(y_values)).tolist()  # Random x values
    initial_result = linear_regression(x_values, y_values)
    x_values[0] += 1.0  # Modify x values slightly
    modified_result = linear_regression(x_values, y_values)
    assert initial_result.slope != modified_result.slope

@given(st.lists(st.floats(), min_size=1))
def test_statistics_error_raised_with_less_than_two_data_points_property(y_values):
    if len(y_values) < 2:
        with pytest.raises(StatisticsError):
            linear_regression([1.0], y_values)  # Only one x value
# End program