from hypothesis import given, strategies as st
import statistics
import math

@given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10)))
def test_slope_is_finite_property(data):
    x, y = data
    slope, _ = statistics.linear_regression(x, y)
    assert not math.isnan(slope) and not math.isinf(slope)

@given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10)))
def test_intercept_is_finite_property(data):
    x, y = data
    _, intercept = statistics.linear_regression(x, y)
    assert not math.isnan(intercept) and not math.isinf(intercept)

@given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10)))
def test_intercept_zero_when_proportional_property(data):
    x, y = data
    slope, intercept = statistics.linear_regression(x, y, proportional=True)
    assert intercept == 0.0

@given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10)))
def test_slope_behavior_with_scaling_property(data):
    x, y = data
    original_slope, _ = statistics.linear_regression(x, y)
    scaled_x = [i * 2 for i in x]
    scaled_slope, _ = statistics.linear_regression(scaled_x, y)
    assert scaled_slope == original_slope * 2

@given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10).filter(lambda lst: len(set(lst)) == 1),
                st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, max_size=10)))
def test_statistics_error_for_constant_x_property(data):
    x = data[0]  # constant value
    y = data[1]
    try:
        statistics.linear_regression(x, y)
        assert False, "Expected StatisticsError was not raised."
    except statistics.StatisticsError:
        pass
# End program