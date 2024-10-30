from hypothesis import given, strategies as st
import statistics
from fractions import Fraction
from decimal import Decimal

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_output_is_number_property(data):
    result = statistics.mean(data)
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_of_identical_values_property(data):
    if len(set(data)) == 1:  # Check if all values are identical
        result = statistics.mean(data)
        assert result == data[0]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_with_negatives_property(data):
    result = statistics.mean(data)
    assert isinstance(result, (float, int, Fraction, Decimal))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_mean_empty_data_raises_error_property(data):
    if not data:
        try:
            statistics.mean(data)
            assert False, "Expected StatisticsError for empty data"
        except statistics.StatisticsError:
            pass  # Expected behavior

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_within_range_property(data):
    result = statistics.mean(data)
    assert result >= min(data) and result <= max(data)
# End program