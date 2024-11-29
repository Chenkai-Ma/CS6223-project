from hypothesis import given, strategies as st
from statistics import pstdev, StatisticsError
import numpy as np

@given(st.lists(st.floats(), min_size=1))
def test_statistics_pstdev_non_negative_property(data):
    result = pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(), min_size=0))
def test_statistics_pstdev_requires_data_property(data):
    if len(data) == 0:
        with pytest.raises(StatisticsError):
            pstdev(data)

@given(st.lists(st.floats(), min_size=1))
def test_statistics_pstdev_single_value_property(data):
    if len(data) == 1:
        result = pstdev(data)
        assert result == 0

@given(st.lists(st.floats()))
def test_statistics_pstdev_order_invariance_property(data):
    result1 = pstdev(data)
    result2 = pstdev(data[::-1])
    assert result1 == result2

@given(st.lists(st.floats(), min_size=2))
def test_statistics_pstdev_variance_relationship_property(data):
    variance = np.var(data, ddof=0)
    result = pstdev(data)
    assert np.isclose(result ** 2, variance)

# End program