from hypothesis import given, strategies as st
from statistics import geometric_mean
import math

@given(st.lists(st.floats(min_value=0, max_value=math.inf), min_size=1, max_size=10))
def test_output_is_positive_property(data):
    result = geometric_mean(data)
    assert result > 0

@given(st.lists(st.floats(min_value=0, max_value=math.inf), min_size=1, max_size=10))
def test_output_le_maximum_value_property(data):
    if data:
        max_value = max(data)
        result = geometric_mean(data)
        assert result <= max_value

@given(st.lists(st.floats(min_value=0, max_value=math.inf), min_size=1, max_size=10))
def test_output_ge_minimum_value_property(data):
    if data:
        min_value = min(data)
        result = geometric_mean(data)
        assert result >= min_value

@given(st.floats(min_value=0, max_value=math.inf))
def test_output_equals_single_value_property(single_value):
    result = geometric_mean([single_value])
    assert result == single_value

@given(st.lists(st.floats(min_value=0, max_value=math.inf), min_size=1, max_size=10))
def test_output_invariant_under_order_property(data):
    result1 = geometric_mean(data)
    result2 = geometric_mean(list(reversed(data)))
    assert result1 == result2
# End program