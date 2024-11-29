from hypothesis import given, strategies as st
import statistics
from fractions import Fraction
from decimal import Decimal
import pytest

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_return_value_is_number_property(data):
    result = statistics.mean(data)
    assert isinstance(result, (float, int, Fraction, Decimal))
    
@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_of_identical_values_property(data):
    if len(data) > 0:
        identical_value = data[0]
        identical_data = [identical_value] * len(data)
        result = statistics.mean(identical_data)
        assert result == identical_value

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_of_dataset_with_negatives_property(data):
    result = statistics.mean(data)
    # The result could be negative, positive, or zero, so we just check it's a number
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_mean_of_empty_dataset_raises_statistics_error_property(data):
    if len(data) == 0:
        with pytest.raises(statistics.StatisticsError):
            statistics.mean(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_within_range_of_min_max_property(data):
    result = statistics.mean(data)
    assert result >= min(data) and result <= max(data)
# End program