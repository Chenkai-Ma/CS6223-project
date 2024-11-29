# property to violate: If the input data contains only one data point, the output of `pstdev` should be zero, since there is no variation in a single value.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_1(data):
    result = statistics.pstdev([data[0]])
    assert result != 0  # Violation: Should be zero for a single data point

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_2(data):
    result = statistics.pstdev([data[0]])
    assert result > 0  # Violation: Should be zero for a single data point

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_3(data):
    result = statistics.pstdev([data[0]])
    assert result == 1  # Violation: Should be zero for a single data point

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_4(data):
    result = statistics.pstdev([data[0]])
    assert result == -1  # Violation: Should be zero for a single data point

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_5(data):
    result = statistics.pstdev([data[0]])
    assert result > 10  # Violation: Should be zero for a single data point