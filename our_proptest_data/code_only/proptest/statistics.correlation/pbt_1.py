from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2), 
           st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_correlation_coefficient_range_property(x, y):
    """The correlation coefficient should always be between -1 and 1."""
    result = statistics.correlation(x, y)
    assert -1 <= result <= 1

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_identical_lists_property(x):
    """If both input lists are identical, the correlation should be 1."""
    result = statistics.correlation(x, x)
    assert result == 1

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_constant_input_property(x):
    """If one of the input lists is constant, it should raise StatisticsError."""
    constant = [1.0] * len(x)
    try:
        statistics.correlation(x, constant)
    except statistics.StatisticsError:
        pass  # Expected behavior
    else:
        assert False, "Expected StatisticsError not raised"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2),
           st.floats())
def test_linear_transformation_property(x, c):
    """For two input lists where the second list is a linear transformation of the first, the correlation should remain 1 or -1."""
    transformed = [xi * c for xi in x]
    result = statistics.correlation(x, transformed)
    assert result == 1 if c > 0 else -1

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2),
           st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_permutation_invariance_property(x, y):
    """The correlation should be invariant under permutations of the input lists."""
    from random import shuffle
    shuffled_x = x[:]
    shuffled_y = y[:]
    shuffle(shuffled_x)
    shuffle(shuffled_y)
    original_result = statistics.correlation(x, y)
    shuffled_result = statistics.correlation(shuffled_x, shuffled_y)
    assert original_result == shuffled_result
# End program