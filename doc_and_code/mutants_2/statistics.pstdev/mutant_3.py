# property to violate: The output of `pstdev` should be equal to the square root of the population variance calculated from the same input data.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_1(data):
    variance = statistics.pvariance(data)
    result = statistics.pstdev(data) + 1  # Adding 1 to the result to violate the property
    assert result == variance ** 0.5

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_2(data):
    variance = statistics.pvariance(data)
    result = statistics.pstdev(data) * 2  # Doubling the result to violate the property
    assert result == variance ** 0.5

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_3(data):
    variance = statistics.pvariance(data)
    result = statistics.pstdev(data) - 5  # Subtracting 5 from the result to violate the property
    assert result == variance ** 0.5

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_4(data):
    variance = statistics.pvariance(data)
    result = statistics.pstdev(data) ** 2  # Squaring the result to violate the property
    assert result == variance ** 0.5

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_5(data):
    variance = statistics.pvariance(data)
    result = -statistics.pstdev(data)  # Negating the result to violate the property
    assert result == variance ** 0.5