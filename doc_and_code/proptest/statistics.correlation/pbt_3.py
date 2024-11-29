from hypothesis import given, strategies as st
from statistics import correlation, StatisticsError

@given(st.lists(st.floats(), min_size=2, max_size=1000))
def test_output_range_property(data):
    x, y = data, data  # Using the same list for simplicity
    result = correlation(x, y)
    assert -1 <= result <= 1

@given(st.lists(st.floats(min_value=0, max_value=1), min_size=2))
def test_constant_input_property(data):
    constant_list = [data[0]] * len(data)
    try:
        correlation(data, constant_list)
        assert False, "Expected StatisticsError due to constant input"
    except StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2), st.floats(), st.floats())
def test_linear_transformation_property(data, scale, shift):
    x = data
    y = [scale * xi + shift for xi in x]
    result = correlation(x, y)
    assert result == 1.0 or result == -1.0

@given(st.lists(st.floats(), min_size=2))
def test_spearman_monotonic_relationship_property(data):
    sorted_data = sorted(data)
    result = correlation(sorted_data, sorted_data, method='ranked')
    assert result == 1.0

@given(st.lists(st.floats(), min_size=2), st.lists(st.floats(), min_size=2))
def test_symmetric_property(x_data, y_data):
    if len(x_data) == len(y_data):
        result_xy = correlation(x_data, y_data)
        result_yx = correlation(y_data, x_data)
        assert result_xy == result_yx
# End program