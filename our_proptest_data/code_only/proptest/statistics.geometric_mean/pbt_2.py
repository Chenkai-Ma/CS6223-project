from hypothesis import given, strategies as st
import math
from statistics import StatisticsError, geometric_mean

@given(st.lists(st.floats(min_value=0.0, allow_nan=True), min_size=1))
def test_geometric_mean_positive_numbers_property(data):
    positive_data = [x for x in data if x > 0]
    if positive_data:
        result = geometric_mean(positive_data)
        assert result > 0

@given(st.lists(st.floats(min_value=0.0, allow_nan=True), min_size=1))
def test_geometric_mean_zero_in_data_property(data):
    if 0.0 in data:
        result = geometric_mean(data)
        assert result == 0.0

@given(st.lists(st.floats(), min_size=0))
def test_geometric_mean_empty_data_property(data):
    if len(data) == 0:
        with st.raises(StatisticsError):
            geometric_mean(data)

@given(st.lists(st.floats(allow_nan=True), min_size=1))
def test_geometric_mean_nan_in_data_property(data):
    if any(math.isnan(x) for x in data):
        result = geometric_mean(data)
        assert math.isnan(result)

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=1))
def test_geometric_mean_negative_numbers_property(data):
    negative_data = [x for x in data if x < 0]
    if negative_data:
        with st.raises(StatisticsError):
            geometric_mean(data)
# End program