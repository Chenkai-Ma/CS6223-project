# property to violate: The output of `pstdev` should always be a non-negative number, as standard deviation cannot be negative.
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
    result = -result - 1  # Make the result negative by subtracting more than the absolute value
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_3(data):
    result = statistics.pstdev(data)
    result = -result + 5  # Shift the result to be negative if the original is less than 5
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_4(data):
    result = statistics.pstdev(data)
    result = -result / 2  # Divide the result by 2 and make it negative
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_5(data):
    result = statistics.pstdev(data)
    result = -result + 10  # Make the result negative by adjusting it to be less than zero
    assert result >= 0