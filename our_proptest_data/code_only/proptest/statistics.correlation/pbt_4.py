from hypothesis import given, strategies as st
from statistics import correlation, StatisticsError

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_correlation_outputs_between_minus_one_and_one_property(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = correlation(x, y)
        assert -1 <= result <= 1

@given(st.lists(st.floats(min_value=1e-10, max_value=1e10), min_size=2))
def test_identical_lists_property(x):
    result = correlation(x, x)
    assert result == 1

@given(st.lists(st.floats(min_value=1e-10, max_value=1e10), min_size=2))
def test_constant_input_property(x):
    constant_list = [x[0]] * len(x)
    try:
        correlation(x, constant_list)
        assert False, "Expected StatisticsError for constant input"
    except StatisticsError:
        pass

@given(st.lists(st.floats()), st.floats(), st.floats())
def test_linear_transformation_property(x, a, b):
    if len(x) >= 2:
        y = [a * xi + b for xi in x]
        result = correlation(x, y)
        assert result == 1 if a > 0 else -1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_permutation_invariance_property(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result1 = correlation(x, y)
        result2 = correlation(y, x)
        assert result1 == result2
# End program