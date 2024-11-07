from hypothesis import given, strategies as st
import numpy as np
from statistics import correlation, StatisticsError

@given(st.lists(st.floats(), min_size=2), st.lists(st.floats(), min_size=2))
def test_correlation_output_range_property(x, y):
    result = correlation(x, y)
    assert -1 <= result <= 1

@given(st.lists(st.floats(), min_size=1))
def test_identical_lists_property(x):
    result = correlation(x, x)
    assert result == 1

@given(st.lists(st.floats(), min_size=1))
def test_constant_input_property(x):
    constant_list = [x[0]] * len(x)
    with st.raises(StatisticsError):
        correlation(x, constant_list)

@given(st.lists(st.floats(), min_size=1), st.floats(), st.floats())
def test_linear_transformation_property(x, a, b):
    transformed_y = [a * xi + b for xi in x]
    result = correlation(x, transformed_y)
    assert result == 1 if a > 0 else -1

@given(st.lists(st.floats(), min_size=2))
def test_permutation_invariance_property(x):
    y = list(x)  # Copy of x
    result1 = correlation(x, y)
    np.random.shuffle(y)  # Shuffle the copy
    result2 = correlation(x, y)
    assert result1 == result2
# End program