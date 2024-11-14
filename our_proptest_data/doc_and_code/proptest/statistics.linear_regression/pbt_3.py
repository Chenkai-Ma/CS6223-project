from hypothesis import given, strategies as st
from statistics import linear_regression, StatisticsError

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1), 
               st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x[0]))))
def test_slope_is_float_property(x, y):
    slope, _ = linear_regression(x, y)
    assert isinstance(slope, float)

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1), 
               st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x[0]))))
def test_intercept_is_float_property(x, y):
    _, intercept = linear_regression(x, y)
    assert isinstance(intercept, float)

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) == 1), 
               st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x[0]))))
def test_constant_x_raises_statistics_error_property(x, y):
    try:
        linear_regression(x, y)
        assert False, "Expected StatisticsError not raised"
    except StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2), 
       st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x[0]))))
def test_identical_x_and_y_yields_slope_one_property(x, y):
    if x == y:
        slope, _ = linear_regression(x, y)
        assert slope == 1.0

@given(st.lists(st.floats(), min_size=2), 
       st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x[0]))))
def test_equal_length_inputs_property(x, y):
    if len(x) != len(y):
        try:
            linear_regression(x, y)
            assert False, "Expected StatisticsError not raised"
        except StatisticsError:
            pass

# End program