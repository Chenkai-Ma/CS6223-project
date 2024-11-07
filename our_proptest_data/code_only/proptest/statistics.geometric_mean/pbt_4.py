from hypothesis import given, strategies as st
import math
from statistics import geometric_mean, StatisticsError

@given(st.lists(st.floats(min_value=0.0, allow_nan=False), min_size=1))
def test_geometric_mean_positive_property(data):
    assert geometric_mean(data) > 0

@given(st.lists(st.floats(min_value=0.0, allow_nan=False), min_size=0))
def test_geometric_mean_zero_property(data):
    assert geometric_mean(data) == 0.0

@given(st.lists(st.floats()))
def test_geometric_mean_empty_dataset_property(data):
    if not data:
        try:
            geometric_mean(data)
            assert False, "Expected StatisticsError for empty dataset"
        except StatisticsError:
            pass

@given(st.lists(st.one_of(st.floats(allow_nan=True), st.floats(min_value=0.0, allow_nan=False)), min_size=1))
def test_geometric_mean_nan_property(data):
    if any(math.isnan(x) for x in data):
        assert math.isnan(geometric_mean(data))

@given(st.lists(st.floats(min_value=-math.inf, max_value=-1.0), min_size=1))
def test_geometric_mean_negative_input_property(data):
    try:
        geometric_mean(data)
        assert False, "Expected StatisticsError for negative inputs"
    except StatisticsError:
        pass
# End program