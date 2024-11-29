from hypothesis import given, strategies as st
from statistics import linear_regression, StatisticsError

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1), 
               st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x))))
def test_slope_is_float_property(x, y):
    slope, intercept = linear_regression(x, y)
    assert isinstance(slope, float)

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1), 
               st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x))))
def test_intercept_is_float_property(x, y):
    slope, intercept = linear_regression(x, y)
    assert isinstance(intercept, float)

@given(st.lists(st.floats(min_value=1, max_value=1000), min_size=3).filter(lambda x: len(set(x)) == 3),
               st.lists(st.floats(min_value=1, max_value=1000), min_size=3).filter(lambda x: len(x) == len(x))))
def test_equal_values_slope_property(x, y):
    slope, intercept = linear_regression(x, y)
    assert slope == 1.0
    assert intercept == 0.0  # This will hold if proportional is true

@given(st.lists(st.floats(min_value=0, max_value=10), min_size=3).filter(lambda x: len(set(x)) == 1), 
               st.lists(st.floats(min_value=0, max_value=10), min_size=3).filter(lambda x: len(x) == len(x))))
def test_constant_x_raises_exception_property(x, y):
    try:
        linear_regression(x, y)
        assert False  # Should not reach this line
    except StatisticsError:
        pass  # Expected behavior

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x)), 
               st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x)).filter(lambda y: len(y) == len(x))))
def test_equal_length_inputs_property(x, y):
    if len(x) != len(y) or len(x) < 2:
        try:
            linear_regression(x, y)
            assert False  # Should not reach this line
        except StatisticsError:
            pass  # Expected behavior
    else:
        slope, intercept = linear_regression(x, y)
        assert isinstance(slope, float) and isinstance(intercept, float)

# End program