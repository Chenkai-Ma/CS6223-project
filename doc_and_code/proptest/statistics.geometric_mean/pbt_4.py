from hypothesis import given, strategies as st
from statistics import geometric_mean, StatisticsError
import math

@given(st.lists(st.floats(min_value=0, allow_nan=True), min_size=1))
def test_geometric_mean_non_empty_property(data):
    result = geometric_mean(data)
    assert isinstance(result, float)  # Output should be a float

@given(st.lists(st.floats(min_value=0, allow_nan=True), min_size=0))
def test_geometric_mean_empty_property(data):
    try:
        geometric_mean(data)
        assert False, "Expected StatisticsError for empty dataset"
    except StatisticsError:
        pass  # Expected behavior

@given(st.lists(st.floats(min_value=0, allow_nan=True), min_size=1))
def test_geometric_mean_zero_property(data):
    data_with_zero = data + [0.0]
    result = geometric_mean(data_with_zero)
    assert result in (0.0, math.nan)  # Should return 0.0 or math.nan if zero is present

@given(st.lists(st.floats(min_value=-math.inf, max_value=-1e-10), min_size=1))
def test_geometric_mean_negative_value_property(data):
    try:
        geometric_mean(data)
        assert False, "Expected StatisticsError for negative inputs"
    except StatisticsError:
        pass  # Expected behavior

@given(st.lists(st.floats(min_value=1e-10, max_value=1e10), min_size=1))
def test_geometric_mean_arithmetic_mean_property(data):
    positive_data = [x for x in data if x > 0]
    if positive_data:
        geom_mean = geometric_mean(positive_data)
        arith_mean = sum(positive_data) / len(positive_data)
        assert geom_mean <= arith_mean  # Geometric mean should be <= arithmetic mean

# End program