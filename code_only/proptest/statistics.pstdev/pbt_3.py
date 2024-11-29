from hypothesis import given, strategies as st
from statistics import pstdev, StatisticsError

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_statistics_pstdev_non_negative_property(data):
    result = pstdev(data)
    assert result >= 0
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_statistics_pstdev_empty_data_property(data):
    if not data:
        with st.raises(StatisticsError):
            pstdev(data)
    else:
        pstdev(data)  # Just to execute the function for non-empty cases
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_statistics_pstdev_single_value_property(data):
    if len(data) == 1:
        result = pstdev(data)
        assert result == 0
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_statistics_pstdev_order_independence_property(data):
    if len(data) > 1:
        result1 = pstdev(data)
        result2 = pstdev(list(reversed(data)))
        assert result1 == result2
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_statistics_pstdev_variance_relationship_property(data):
    variance = sum((x - sum(data) / len(data)) ** 2 for x in data) / len(data)
    result = pstdev(data)
    assert result**2 == variance
# End program