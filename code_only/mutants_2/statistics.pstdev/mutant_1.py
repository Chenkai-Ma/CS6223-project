# property to violate: The output of `pstdev` should always be non-negative, as standard deviation cannot be negative.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_1(data):
    result = statistics.pstdev(data)
    result = -abs(result)  # Force the result to be negative
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_2(data):
    result = statistics.pstdev(data)
    result = result - (result + 1)  # Shift the result to be negative
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_3(data):
    result = statistics.pstdev(data)
    result = -result + 1  # Make the result positive but then negate it
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_4(data):
    result = statistics.pstdev(data)
    result = -(result / 2)  # Halve the result and negate it
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_5(data):
    result = statistics.pstdev(data)
    result = -result - 100  # Force the result to be a large negative number
    assert result >= 0