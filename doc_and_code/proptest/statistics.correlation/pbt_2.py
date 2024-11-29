from hypothesis import given, strategies as st
import statistics
from statistics import StatisticsError

@given(st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda x: len(set(x)) > 1),
                unique=True), st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda x: len(set(x)) > 1,
                unique=True))
def test_output_within_bounds_property(x, y):
    result = statistics.correlation(x, y)
    assert -1 <= result <= 1

@given(st.lists(st.floats(), min_size=2, max_size=1000, unique=True))
def test_constant_input_raises_property(x):
    with st.raises(StatisticsError):
        statistics.correlation(x, x)

@given(st.lists(st.floats(), min_size=2, max_size=1000), st.floats(), st.floats())
def test_linear_transformation_property(x, a, b):
    y = [a * xi + b for xi in x]
    result = statistics.correlation(x, y)
    assert result == 1.0 or result == -1.0

@given(st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda x: len(set(x)) > 1),
                unique=True), st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda x: len(set(x)) > 1,
                unique=True))
def test_spearman_monotonic_relationship_property(x, y):
    result = statistics.correlation(x, y, method='ranked')
    if sorted(x) == sorted(y):
        assert result == 1.0

@given(st.lists(st.floats(), min_size=2, max_size=1000), st.lists(st.floats(), min_size=2, max_size=1000))
def test_symmetric_property(x, y):
    result_xy = statistics.correlation(x, y)
    result_yx = statistics.correlation(y, x)
    assert result_xy == result_yx
# End program