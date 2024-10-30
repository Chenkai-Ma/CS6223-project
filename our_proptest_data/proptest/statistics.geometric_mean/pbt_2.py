from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(min_value=0.1, max_value=1e10), min_size=1, max_size=5))
def test_geometric_mean_positive_output_property(data):
    result = statistics.geometric_mean(data)
    assert result > 0

@given(st.lists(st.floats(min_value=0.1, max_value=1e10), min_size=1, max_size=5))
def test_geometric_mean_maximum_value_property(data):
    result = statistics.geometric_mean(data)
    assert result <= max(data)

@given(st.lists(st.floats(min_value=0.1, max_value=1e10), min_size=1, max_size=5))
def test_geometric_mean_minimum_value_property(data):
    result = statistics.geometric_mean(data)
    assert result >= min(data)

@given(st.floats(min_value=0.1, max_value=1e10))
def test_geometric_mean_single_value_property(value):
    result = statistics.geometric_mean([value])
    assert result == value

@given(st.lists(st.floats(min_value=0.1, max_value=1e10), min_size=2, max_size=5))
def test_geometric_mean_order_invariance_property(data):
    result1 = statistics.geometric_mean(data)
    result2 = statistics.geometric_mean(list(reversed(data)))
    assert result1 == result2
# End program