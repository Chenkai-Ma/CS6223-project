from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1), 
                st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2, unique=True)))
def test_slope_is_finite_property(data):
    x, y = data
    slope, intercept = statistics.linear_regression(x, y)
    assert not (slope != slope or slope == float('inf') or slope == float('-inf'))

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1), 
                st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2, unique=True)))
def test_intercept_is_finite_property(data):
    x, y = data
    slope, intercept = statistics.linear_regression(x, y)
    assert not (intercept != intercept or intercept == float('inf') or intercept == float('-inf'))

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1), 
                st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2, unique=True)))
def test_intercept_zero_if_proportional_property(data):
    x, y = data
    slope, intercept = statistics.linear_regression(x, y, proportional=True)
    assert intercept == 0.0

@given(st.lists(st.floats(min_value=1e-6, max_value=1e6), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1), 
                st.lists(st.floats(min_value=1e-6, max_value=1e6), min_size=2, unique=True)))
def test_slope_changes_predictably_property(data):
    x, y = data
    original_slope, _ = statistics.linear_regression(x, y)
    scaled_x = [i * 2 for i in x]
    new_slope, _ = statistics.linear_regression(scaled_x, y)
    assert new_slope == 2 * original_slope

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2, unique=True).filter(lambda x: len(set(x)) == 1), 
                st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2, unique=True)))
def test_statistics_error_if_constant_x_property(data):
    x, y = data
    try:
        statistics.linear_regression(x, y)
        assert False  # Should raise an error
    except statistics.StatisticsError:
        assert True

# End program