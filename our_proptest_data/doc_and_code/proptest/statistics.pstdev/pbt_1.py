from hypothesis import given, strategies as st
import statistics
from statistics import StatisticsError
import math

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_pstdev_non_negative_property(data):
    result = statistics.pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_pstdev_single_element_property(data):
    if len(data) == 1:
        result = statistics.pstdev(data)
        assert result == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_pstdev_variance_property(data):
    variance = statistics.pvariance(data)
    result = statistics.pstdev(data)
    assert math.isclose(result, math.sqrt(variance))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_pstdev_empty_data_property(data):
    if len(data) == 0:
        try:
            statistics.pstdev(data)
            assert False, "Expected StatisticsError for empty data."
        except StatisticsError:
            pass

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_pstdev_repeatability_property(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data)
    assert result1 == result2
# End program