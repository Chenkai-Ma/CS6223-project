from hypothesis import given, strategies as st
import statistics
from statistics import StatisticsError

@given(st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1),
                st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1))
@given(st.lists(st.floats(min_value=1, max_value=1000), min_size=2, max_size=1000))
def test_correlation_output_range_property(x, y):
    result = statistics.correlation(x, y)
    assert -1 <= result <= 1

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) == 1),
               st.lists(st.floats(), min_size=2))
def test_correlation_constant_input_property(x, y):
    try:
        statistics.correlation(x, y)
        assert False, "Expected StatisticsError but function executed successfully."
    except StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) > 1),
               st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) > 1))
def test_correlation_linear_transformation_property(x, y):
    # Scale and shift
    scaled_y = [2 * val + 3 for val in y]
    assert statistics.correlation(x, y) == statistics.correlation(x, scaled_y)

@given(st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1),
                st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1))
def test_correlation_spearman_monotonic_property(x, y):
    sorted_x = sorted(x)
    sorted_y = sorted(y)
    assert statistics.correlation(sorted_x, sorted_y, method='ranked') == 1.0

@given(st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1),
                st.lists(st.floats(), min_size=2, max_size=1000).filter(lambda lst: len(set(lst)) > 1))
def test_correlation_symmetry_property(x, y):
    assert statistics.correlation(x, y) == statistics.correlation(y, x)

# End program