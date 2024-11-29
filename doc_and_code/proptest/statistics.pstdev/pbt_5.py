from hypothesis import given, strategies as st
from statistics import pstdev, StatisticsError
import math

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_output_non_negative_property(data):
    result = pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_single_element_zero_property(data):
    if len(data) == 1:
        result = pstdev(data)
        assert result == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_output_equals_sqrt_variance_property(data):
    result = pstdev(data)
    variance = sum((x - sum(data) / len(data)) ** 2 for x in data) / len(data)
    assert math.isclose(result, math.sqrt(variance))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_empty_data_raises_error_property(data):
    if len(data) == 0:
        try:
            pstdev(data)
            assert False, "Expected StatisticsError for empty data"
        except StatisticsError:
            pass

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_repeated_calls_consistent_property(data):
    result1 = pstdev(data)
    result2 = pstdev(data)
    assert result1 == result2
# End program