from hypothesis import given, strategies as st
from statistics import linear_regression, StatisticsError

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1), 
               st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1))
)
def test_slope_property(x, y):
    slope, intercept = linear_regression(x, y)
    assert isinstance(slope, float)  # Slope should be a float.

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1), 
               st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1))
)
def test_intercept_property(x, y):
    slope, intercept = linear_regression(x, y)
    assert isinstance(intercept, float)  # Intercept should be a float.

@given(st.lists(st.floats(), min_size=3).filter(lambda x: len(set(x)) == len(x)), 
               st.lists(st.floats(), min_size=3).filter(lambda x: len(set(x)) == len(x)))
)
def test_equal_values_property(x, y):
    # When x and y are equal, the slope should be 1 and intercept should be 0.
    slope, intercept = linear_regression(x, x)
    assert slope == 1
    assert intercept == 0

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) == 1), 
               st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1))
)
def test_constant_x_property(y, constant_x):
    # When x is constant, expect a StatisticsError
    try:
        linear_regression(constant_x, y)
        assert False, "Expected StatisticsError for constant x"
    except StatisticsError:
        pass  # This is the expected outcome.

@given(st.lists(st.floats(), min_size=2), 
       st.lists(st.floats(), min_size=2).filter(lambda x: len(x) == len(x)))
)
def test_input_length_property(x, y):
    # Check that both inputs have the same length
    if len(x) != len(y):
        try:
            linear_regression(x, y)
            assert False, "Expected StatisticsError for unequal lengths"
        except StatisticsError:
            pass  # This is the expected outcome.
    else:
        # If they are equal, we should not raise an error.
        slope, intercept = linear_regression(x, y)
        assert isinstance(slope, float)
        assert isinstance(intercept, float)

# End program