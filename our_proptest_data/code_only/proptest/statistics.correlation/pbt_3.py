from hypothesis import given, strategies as st
import statistics  # Assuming the correlation function is in a module named statistics
from statistics import StatisticsError

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_correlation_output_range_property(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y)
        assert -1 <= result <= 1

@given(st.lists(st.floats()))
def test_correlation_identical_lists_property(x):
    if len(x) >= 2:
        result = statistics.correlation(x, x)
        assert result == 1

@given(st.lists(st.floats(), min_size=2))
def test_correlation_constant_input_property(x):
    constant_list = [x[0]] * len(x)
    try:
        statistics.correlation(x, constant_list)
        assert False  # Should not reach this line
    except StatisticsError:
        pass

@given(st.lists(st.floats()), st.floats(), st.floats())
def test_correlation_linear_transformation_property(x, scale, shift):
    if len(x) >= 2:
        y = [scale * xi + shift for xi in x]
        result = statistics.correlation(x, y)
        assert result == 1 if scale > 0 else -1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_correlation_permutation_invariance_property(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result_original = statistics.correlation(x, y)
        result_permuted = statistics.correlation(sorted(x), sorted(y))
        assert result_original == result_permuted
# End program