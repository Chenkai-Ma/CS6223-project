from hypothesis import given, strategies as st
from statistics import pstdev, StatisticsError
import math

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_statistics_pstdev_non_negative_property(data):
    result = pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_statistics_pstdev_empty_input_property(data):
    if len(data) == 0:
        try:
            pstdev(data)
            assert False, "Expected StatisticsError for empty input"
        except StatisticsError:
            pass

@given(st.floats())
def test_statistics_pstdev_single_value_property(value):
    result = pstdev([value])
    assert result == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_statistics_pstdev_order_independence_property(data):
    result1 = pstdev(data)
    result2 = pstdev(data[::-1])  # Reverse the list
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_statistics_pstdev_variance_relationship_property(data):
    variance = sum((x - sum(data) / len(data)) ** 2 for x in data) / len(data)
    result = pstdev(data)
    assert math.isclose(result, math.sqrt(variance))
# End program