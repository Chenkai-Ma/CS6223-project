from hypothesis import given, strategies as st
import math
from statistics import geometric_mean, StatisticsError

@given(st.lists(st.floats(allow_nan=False, min_value=0.1, max_value=1e10), min_size=1))
def test_geometric_mean_positive_numbers_property(data):
    result = geometric_mean(data)
    assert result > 0

@given(st.lists(st.floats(allow_nan=False, min_value=0.0, max_value=1e10), min_size=1))
def test_geometric_mean_zero_included_property(data):
    if 0.0 in data:
        result = geometric_mean(data)
        assert result == 0.0

@given(st.lists(st.floats(allow_nan=False, min_value=-1e10, max_value=1e10), min_size=0))
def test_geometric_mean_empty_dataset_property(data):
    if len(data) == 0:
        with pytest.raises(StatisticsError):
            geometric_mean(data)

@given(st.lists(st.floats(allow_nan=True, min_value=-1e10, max_value=1e10), min_size=1))
def test_geometric_mean_nan_included_property(data):
    if any(math.isnan(x) for x in data):
        result = geometric_mean(data)
        assert math.isnan(result)

@given(st.lists(st.floats(min_value=-1e10, max_value=0.0), min_size=1))
def test_geometric_mean_negative_numbers_property(data):
    with pytest.raises(StatisticsError):
        geometric_mean(data)
# End program