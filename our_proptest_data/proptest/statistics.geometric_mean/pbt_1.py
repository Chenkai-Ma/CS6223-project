from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1, max_size=5))
def test_output_is_positive_property(data):
    result = statistics.geometric_mean(data)
    assert result > 0

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1, max_size=5))
def test_output_less_than_or_equal_to_max_property(data):
    result = statistics.geometric_mean(data)
    assert result <= max(data)

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1, max_size=5))
def test_output_greater_than_or_equal_to_min_property(data):
    result = statistics.geometric_mean(data)
    assert result >= min(data)

@given(st.floats(min_value=0.0001, max_value=1e10))
def test_output_equals_single_value_property(single_value):
    result = statistics.geometric_mean([single_value])
    assert result == single_value

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1, max_size=5))
def test_output_invariant_under_order_property(data):
    result_original = statistics.geometric_mean(data)
    result_sorted = statistics.geometric_mean(sorted(data))
    assert result_original == result_sorted
# End program