from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(min_value=0.1, max_value=1e10), min_size=1, max_size=100))
def test_output_is_positive_property(data):
    result = statistics.geometric_mean(data)
    assert result > 0

@given(st.lists(st.floats(min_value=0.1, max_value=1e10), min_size=1, max_size=100))
def test_output_less_than_or_equal_to_max_property(data):
    result = statistics.geometric_mean(data)
    assert result <= max(data)

@given(st.lists(st.floats(min_value=0.1, max_value=1e10), min_size=1, max_size=100))
def test_output_greater_than_or_equal_to_min_property(data):
    result = statistics.geometric_mean(data)
    assert result >= min(data)

@given(st.floats(min_value=0.1, max_value=1e10))
def test_output_equals_single_value_property(value):
    result = statistics.geometric_mean([value])
    assert result == value

@given(st.lists(st.floats(min_value=0.1, max_value=1e10), min_size=1, max_size=100))
def test_output_invariant_under_order_property(data):
    result1 = statistics.geometric_mean(data)
    result2 = statistics.geometric_mean(sorted(data))
    assert result1 == result2
# End program