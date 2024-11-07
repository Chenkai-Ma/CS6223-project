from hypothesis import given, strategies as st
import math
from statistics import geometric_mean, StatisticsError

@given(st.lists(st.floats(min_value=0, allow_nan=False, exclude_min=True), min_size=1))
def test_geometric_mean_positive_numbers_property(data):
    result = geometric_mean(data)
    assert result > 0

@given(st.lists(st.floats(min_value=0, allow_nan=False, exclude_min=True), min_size=0))
def test_geometric_mean_zero_property(data):
    if 0.0 in data:
        result = geometric_mean(data)
        assert result == 0.0
    else:
        result = geometric_mean(data)
        assert isinstance(result, float)

@given(st.lists(st.floats(allow_nan=False), min_size=0))
def test_geometric_mean_empty_dataset_property(data):
    if not data:
        try:
            geometric_mean(data)
            assert False, "Expected StatisticsError for empty dataset"
        except StatisticsError:
            pass

@given(st.lists(st.one_of(st.floats(allow_nan=False, min_value=-1e10, max_value=-1e-1), st.floats(allow_nan=True)), min_size=1))
def test_geometric_mean_nan_values_property(data):
    if any(math.isnan(x) for x in data):
        result = geometric_mean(data)
        assert math.isnan(result)
    else:
        result = geometric_mean(data)
        assert isinstance(result, float)

@given(st.lists(st.floats(min_value=-1e10, max_value=-1e-1), min_size=1))
def test_geometric_mean_negative_numbers_property(data):
    try:
        geometric_mean(data)
        assert False, "Expected StatisticsError for negative inputs"
    except StatisticsError:
        pass
# End program