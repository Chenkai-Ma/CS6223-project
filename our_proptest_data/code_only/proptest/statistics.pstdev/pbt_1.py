from hypothesis import given, strategies as st
from statistics import pstdev, StatisticsError
import math

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_statistics_pstdev_non_negative_output(data):
    result = pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)).filter(lambda x: len(x) == 0))
def test_statistics_pstdev_empty_data_raises_error(data):
    with st.raises(StatisticsError):
        pstdev(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)).filter(lambda x: len(x) == 1))
def test_statistics_pstdev_single_data_point_zero(data):
    result = pstdev(data)
    assert result == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_statistics_pstdev_order_independence(data):
    result1 = pstdev(data)
    result2 = pstdev(data[::-1])
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)).filter(lambda x: len(x) > 1))
def test_statistics_pstdev_equivalence_to_sqrt_variance(data):
    variance = sum((x - sum(data) / len(data)) ** 2 for x in data) / len(data)
    result = pstdev(data)
    assert math.isclose(result, math.sqrt(variance), rel_tol=1e-9)

# End program