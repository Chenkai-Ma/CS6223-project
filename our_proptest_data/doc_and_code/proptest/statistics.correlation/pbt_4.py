from hypothesis import given, strategies as st
from statistics import correlation, StatisticsError

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1),
               st.lists(st.floats(), min_size=2).filter(lambda y: len(set(y)) > 1))
def test_output_range_property(x, y):
    result = correlation(x, y)
    assert -1 <= result <= 1

@given(st.lists(st.floats(), min_size=2).map(lambda x: [x[0]] * len(x)),
               st.lists(st.floats(), min_size=2).map(lambda y: [y[0]] * len(y)))
def test_constant_input_property(x, y):
    try:
        correlation(x, y)
        assert False, "Expected StatisticsError for constant inputs"
    except StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1),
               st.lists(st.floats(), min_size=2).filter(lambda y: len(set(y)) > 1))
def test_linear_transformation_property(x, y):
    scale = st.floats(min_value=0.1, max_value=10.0).example()
    shifted_y = [scale * val + 1 for val in y]
    result = correlation(x, shifted_y)
    assert result == 1.0 or result == -1.0

@given(st.lists(st.floats(), min_size=2),
       st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1))
def test_ranked_monotonic_property(x, y):
    result = correlation(x, y, method='ranked')
    assert result == 1.0 or result == -1.0

@given(st.lists(st.floats(), min_size=2),
       st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) > 1))
def test_symmetric_property(x, y):
    result_xy = correlation(x, y)
    result_yx = correlation(y, x)
    assert result_xy == result_yx
# End program