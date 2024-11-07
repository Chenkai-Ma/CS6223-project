from hypothesis import given, strategies as st
from statistics import pstdev, StatisticsError

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_statistics_pstdev_non_negative_property(data):
    result = pstdev(data)
    assert result >= 0
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_statistics_pstdev_empty_input_property(data):
    if len(data) == 0:
        try:
            pstdev(data)
            assert False, "Expected StatisticsError for empty input"
        except StatisticsError:
            pass
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_statistics_pstdev_single_value_property(data):
    result = pstdev([data[0]])
    assert result == 0
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_statistics_pstdev_order_invariance_property(data):
    result1 = pstdev(data)
    result2 = pstdev(data[::-1])
    assert result1 == result2
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_statistics_pstdev_variance_relationship_property(data):
    variance = sum((x - sum(data)/len(data)) ** 2 for x in data) / len(data)
    result = pstdev(data)
    assert result ** 2 == variance
# End program