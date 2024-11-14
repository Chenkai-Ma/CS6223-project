from hypothesis import given, strategies as st
import statistics
from statistics import StatisticsError

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) > 1), 
               st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) > 1))
def test_output_range_property(x, y):
    result = statistics.correlation(x, y)
    assert -1 <= result <= 1

@given(st.lists(st.floats(), min_size=2).map(lambda lst: [lst[0]] * len(lst)))
def test_constant_input_property(x):
    with st.raises(StatisticsError):
        statistics.correlation(x, x)

@given(st.lists(st.floats(), min_size=2), 
       st.floats(), 
       st.floats())
def test_linear_transformation_property(x, a, b):
    transformed_x = [a * xi + b for xi in x]
    result_original = statistics.correlation(x, transformed_x)
    assert result_original == 1.0 or result_original == -1.0

@given(st.lists(st.floats(), min_size=2), 
       st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) > 1))
def test_spearman_monotonic_property(x, y):
    assert statistics.correlation(x, y, method='ranked') == 1.0

@given(st.lists(st.floats(), min_size=2), 
       st.lists(st.floats(), min_size=2))
def test_symmetry_property(x, y):
    result_xy = statistics.correlation(x, y)
    result_yx = statistics.correlation(y, x)
    assert result_xy == result_yx
# End program