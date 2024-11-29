from hypothesis import given, strategies as st
import math
from statistics import geometric_mean, StatisticsError

@given(st.lists(st.floats(min_value=0, allow_nan=False), min_size=1))
def test_output_is_float_property(data):
    result = geometric_mean(data)
    assert isinstance(result, float)

@given(st.lists(st.floats(min_value=0, allow_nan=False), min_size=0))
def test_empty_input_raises_property(data):
    if len(data) == 0:
        with st.raises(StatisticsError):
            geometric_mean(data)

@given(st.lists(st.floats(min_value=-math.inf, max_value=math.inf), min_size=1))
def test_zero_in_input_returns_zero_property(data):
    if 0.0 in data:
        result = geometric_mean(data)
        assert result == 0.0 or math.isnan(result)

@given(st.lists(st.floats(min_value=-math.inf, max_value=math.inf), min_size=1))
def test_negative_input_raises_property(data):
    if any(x < 0 for x in data):
        with st.raises(StatisticsError):
            geometric_mean(data)

@given(st.lists(st.floats(min_value=0, allow_nan=False), min_size=1))
def test_geometric_mean_less_than_arithmetic_mean_property(data):
    if all(x > 0 for x in data):
        geom_mean = geometric_mean(data)
        arith_mean = sum(data) / len(data)
        assert geom_mean <= arith_mean
# End program