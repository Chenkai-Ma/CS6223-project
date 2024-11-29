from hypothesis import given, strategies as st
import statistics
from fractions import Fraction
from decimal import Decimal
import numpy as np

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_output_is_number_property(data):
    result = statistics.mean(data)
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_identical_values_property(data):
    if len(set(data)) == 1:  # Only test if all elements are identical
        result = statistics.mean(data)
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_includes_negatives_property(data):
    result = statistics.mean(data)
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_mean_empty_dataset_raises_property(data):
    if len(data) == 0:
        try:
            statistics.mean(data)
            assert False  # Should not reach this line
        except statistics.StatisticsError:
            pass  # This is expected

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_within_range_property(data):
    result = statistics.mean(data)
    assert result >= min(data) and result <= max(data)
# End program