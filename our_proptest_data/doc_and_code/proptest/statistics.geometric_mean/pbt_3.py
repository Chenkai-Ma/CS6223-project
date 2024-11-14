from hypothesis import given, strategies as st
import math
from statistics import geometric_mean, StatisticsError

@given(st.lists(st.floats(min_value=0, allow_nan=False), min_size=1))
def test_non_empty_positive_inputs_property(data):
    result = geometric_mean(data)
    assert isinstance(result, float)

@given(st.lists(st.floats(min_value=0, allow_nan=False), min_size=0))
def test_empty_input_property(data):
    with st.raises(StatisticsError):
        geometric_mean(data)

@given(st.lists(st.floats(min_value=0, allow_nan=False), min_size=1))
def test_zero_input_property(data):
    data_with_zero = data + [0.0]
    result = geometric_mean(data_with_zero)
    assert result == 0.0 or math.isnan(result)

@given(st.lists(st.floats(min_value=-math.inf, max_value=0, allow_nan=False), min_size=1))
def test_negative_input_property(data):
    with st.raises(StatisticsError):
        geometric_mean(data)

@given(st.lists(st.floats(min_value=1e-10, max_value=1e10, allow_nan=False), min_size=1))
def test_geometric_mean_less_than_arithmetic_mean_property(data):
    geom_mean = geometric_mean(data)
    arith_mean = sum(data) / len(data)
    assert geom_mean <= arith_mean
# End program