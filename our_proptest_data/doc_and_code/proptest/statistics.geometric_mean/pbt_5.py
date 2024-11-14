from hypothesis import given, strategies as st
from statistics import geometric_mean, StatisticsError
import math

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1))
def test_geometric_mean_positive_values_property(data):
    result = geometric_mean(data)
    assert isinstance(result, float)  # Output should be a float
    assert all(x > 0 for x in data)  # Input values are positive

@given(st.lists(st.floats(), min_size=0))
def test_geometric_mean_empty_input_property(data):
    if len(data) == 0:
        with st.raises(StatisticsError):
            geometric_mean(data)

@given(st.lists(st.floats(min_value=0, max_value=1e10), min_size=1))
def test_geometric_mean_zero_input_property(data):
    data.append(0.0)  # Ensure there's a zero in the data
    result = geometric_mean(data)
    assert result in (0.0, math.nan)  # Output should be 0.0 or NaN

@given(st.lists(st.floats(min_value=-1e10, max_value=0), min_size=1))
def test_geometric_mean_negative_input_property(data):
    with st.raises(StatisticsError):
        geometric_mean(data)

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1))
def test_geometric_mean_arithmetic_vs_geometric_property(data):
    arithmetic_mean = sum(data) / len(data)
    result = geometric_mean(data)
    assert result <= arithmetic_mean  # Geometric mean should be <= arithmetic mean
# End program