# property to violate: If both input lists have the same values (e.g., x = [1, 2, 3] and y = [1, 2, 3]), the slope should be equal to 1 and the intercept should be 0 (or undefined when proportional is true).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_1(x, y):
    constant_x = [1] * len(y)
    constant_y = [2] * len(y)  # Change y to a constant value different from x
    statistics.linear_regression(constant_x, constant_y)
    assert False, "Expected StatisticsError for constant x"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_2(x, y):
    constant_x = [0] * len(y)  # x is constant
    constant_y = [1] * len(y)  # y is also constant but different from x
    statistics.linear_regression(constant_x, constant_y)
    assert False, "Expected StatisticsError for constant x"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_3(x, y):
    constant_x = [3] * len(y)  # x is constant
    constant_y = [4] * len(y)  # y is also constant but different from x
    statistics.linear_regression(constant_x, constant_y)
    assert False, "Expected StatisticsError for constant x"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_4(x, y):
    constant_x = [2] * len(y)  # x is constant
    constant_y = [5] * len(y)  # y is also constant but different from x
    statistics.linear_regression(constant_x, constant_y)
    assert False, "Expected StatisticsError for constant x"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_violation_of_statistics_linear_regression_5(x, y):
    constant_x = [7] * len(y)  # x is constant
    constant_y = [8] * len(y)  # y is also constant but different from x
    statistics.linear_regression(constant_x, constant_y)
    assert False, "Expected StatisticsError for constant x"