# property to violate: If both input lists have the same values (e.g., x = [1, 2, 3] and y = [1, 2, 3]), the slope should be equal to 1 and the intercept should be 0 (or undefined when proportional is true).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_1(x, y):
    constant_x = [5] * len(y)
    slope, intercept = statistics.linear_regression(constant_x, y)
    assert slope != 1 or intercept != 0, "Expected slope to not be 1 or intercept to not be 0"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_2(x, y):
    constant_x = [5] * len(y)
    slope, intercept = statistics.linear_regression(constant_x, y)
    assert slope > 1, "Expected slope to be greater than 1"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_3(x, y):
    constant_x = [5] * len(y)
    slope, intercept = statistics.linear_regression(constant_x, y)
    assert intercept != 0, "Expected intercept to not be 0"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_4(x, y):
    constant_x = [5] * len(y)
    slope, intercept = statistics.linear_regression(constant_x, y)
    assert slope < 1, "Expected slope to be less than 1"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_5(x, y):
    constant_x = [5] * len(y)
    slope, intercept = statistics.linear_regression(constant_x, y)
    assert slope != 1 and intercept != 0, "Expected slope to not be 1 and intercept to not be 0"