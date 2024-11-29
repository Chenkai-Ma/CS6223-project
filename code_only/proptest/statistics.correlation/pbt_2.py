from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=2, max_size=100), st.lists(st.floats(), min_size=2, max_size=100))
def test_correlation_between_neg1_and_1_property(x, y):
    if len(x) == len(y):
        result = statistics.correlation(x, y)
        assert -1 <= result <= 1

@given(st.lists(st.floats(), min_size=2, max_size=100))
def test_identical_lists_correlation_property(x):
    result = statistics.correlation(x, x)
    assert result == 1

@given(st.lists(st.floats(), min_size=2, max_size=100))
def test_constant_list_correlation_property(x):
    constant_value = x[0]
    x_constant = [constant_value] * len(x)
    try:
        statistics.correlation(x_constant, x)
        assert False  # This should not be reached
    except statistics.StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2, max_size=100), st.floats(), st.floats())
def test_linear_transformation_correlation_property(x, a, b):
    if len(x) > 0:
        y = [a * xi + b for xi in x]
        result = statistics.correlation(x, y)
        assert result == 1 if a > 0 else -1

@given(st.lists(st.floats(), min_size=2, max_size=100))
def test_permutation_invariance_property(x):
    if len(x) > 0:
        y = x[:]
        shuffled_y = y.copy()
        import random
        random.shuffle(shuffled_y)
        result_original = statistics.correlation(x, y)
        result_shuffled = statistics.correlation(x, shuffled_y)
        assert result_original == result_shuffled
# End program