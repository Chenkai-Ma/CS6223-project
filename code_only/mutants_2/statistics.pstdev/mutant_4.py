# property to violate: The output of `pstdev` should be consistent with the output of `pstdev` when the input data is the same, regardless of the order of the data points.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_1(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data[::-1]) + 1  # Adding 1 to the result to violate the property
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_2(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data[::-1]) * 2  # Doubling the result to violate the property
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_3(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data[::-1]) - 5  # Subtracting 5 from the result to violate the property
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_4(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data[::-1]) ** 2  # Squaring the result to violate the property
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_5(data):
    result1 = statistics.pstdev(data)
    result2 = -statistics.pstdev(data[::-1])  # Negating the result to violate the property
    assert result1 == result2