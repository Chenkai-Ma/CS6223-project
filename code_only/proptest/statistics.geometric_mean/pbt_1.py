from hypothesis import given, strategies as st
import math
from statistics import geometric_mean, StatisticsError

@given(st.lists(st.floats(min_value=0, allow_nan=True, allow_infinity=False), min_size=1))
def test_geometric_mean_positive_numbers_property(data):
    # Filter out NaN values and ensure we are only dealing with positive numbers
    data = [x for x in data if x > 0]
    if data:
        result = geometric_mean(data)
        assert result > 0

@given(st.lists(st.floats(min_value=0, max_value=0, allow_nan=False), min_size=1))
def test_geometric_mean_zero_property(data):
    result = geometric_mean(data)
    assert result == 0.0

@given(st.lists(st.floats(), min_size=0))
def test_geometric_mean_empty_dataset_property(data):
    try:
        geometric_mean(data)
        assert False  # Should not reach this line
    except StatisticsError as e:
        assert str(e) == 'Must have a non-empty dataset'

@given(st.lists(st.floats(allow_nan=True), min_size=1))
def test_geometric_mean_nan_in_dataset_property(data):
    data.append(float('nan'))  # Ensure there's at least one NaN
    result = geometric_mean(data)
    assert math.isnan(result)

@given(st.lists(st.floats(min_value=float('-inf'), max_value=-1), min_size=1))
def test_geometric_mean_negative_numbers_property(data):
    try:
        geometric_mean(data)
        assert False  # Should not reach this line
    except StatisticsError as e:
        assert str(e) == 'No negative inputs allowed'
# End program