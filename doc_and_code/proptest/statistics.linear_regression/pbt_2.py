from hypothesis import given, strategies as st
import statistics
from statistics import StatisticsError

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_slope_output_property(x, y):
    slope, intercept = statistics.linear_regression(x, y)
    assert isinstance(slope, float)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_intercept_output_property(x, y):
    slope, intercept = statistics.linear_regression(x, y)
    assert isinstance(intercept, float)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_constant_input_property(x, y):
    constant_x = [5] * len(y)
    try:
        statistics.linear_regression(constant_x, y)
        assert False, "Expected StatisticsError for constant x"
    except StatisticsError:
        pass

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000).filter(lambda lst: len(lst) == len(x)))
def test_equal_input_values_property(x, y):
    same_values = [1] * len(x)
    slope, intercept = statistics.linear_regression(same_values, same_values)
    assert slope == 1
    assert intercept == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000), 
                st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000).filter(lambda lst: len(lst) == len(x)))
def test_length_check_property(x, y):
    if len(x) != len(y):
        try:
            statistics.linear_regression(x, y)
            assert False, "Expected StatisticsError due to unequal lengths"
        except StatisticsError:
            pass
    if len(x) < 2:
        try:
            statistics.linear_regression(x, y)
            assert False, "Expected StatisticsError due to less than two points"
        except StatisticsError:
            pass
# End program