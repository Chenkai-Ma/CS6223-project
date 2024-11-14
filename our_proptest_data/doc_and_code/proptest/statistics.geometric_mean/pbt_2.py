from hypothesis import given, strategies as st
import math
from statistics import geometric_mean, StatisticsError

@given(st.lists(st.floats(min_value=0, allow_nan=False), min_size=1))
def test_geometric_mean_non_empty_property(data):
    result = geometric_mean(data)
    assert isinstance(result, float)

@given(st.lists(st.floats(), min_size=0))
def test_geometric_mean_empty_input_property(data):
    if not data:
        try:
            geometric_mean(data)
            assert False, "Expected StatisticsError for empty input"
        except StatisticsError:
            pass

@given(st.lists(st.floats(min_value=0, allow_nan=False), min_size=1))
def test_geometric_mean_zero_input_property(data):
    data_with_zero = data + [0.0]
    result = geometric_mean(data_with_zero)
    assert result == 0.0 or math.isnan(result)

@given(st.lists(st.floats(min_value=-math.inf, max_value=-1e-10), min_size=1))
def test_geometric_mean_negative_input_property(data):
    try:
        geometric_mean(data)
        assert False, "Expected StatisticsError for negative input"
    except StatisticsError:
        pass

@given(st.lists(st.floats(min_value=1e-10, max_value=1e10), min_size=2))
def test_geometric_mean_relational_property(data):
    arithmetic_mean = sum(data) / len(data)
    result = geometric_mean(data)
    assert result <= arithmetic_mean

# End program