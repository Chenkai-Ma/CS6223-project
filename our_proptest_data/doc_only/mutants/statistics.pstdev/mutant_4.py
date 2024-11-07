# property to violate: The output should be equal to the square root of the output from the `pvariance()` function when the same input data is provided.
from hypothesis import given, strategies as st
import statistics

@given(st.data())
def test_violation_of_statistics_pstdev_1(data):
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev != result_pvariance  # Violation: use != instead of ==

@given(st.data())
def test_violation_of_statistics_pstdev_2(data):
    result_pstdev = statistics.pstdev(data) + 1  # Violation: add 1 to the result
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev == result_pvariance

@given(st.data())
def test_violation_of_statistics_pstdev_3(data):
    result_pstdev = statistics.pstdev(data) * 2  # Violation: multiply the result by 2
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev == result_pvariance

@given(st.data())
def test_violation_of_statistics_pstdev_4(data):
    result_pstdev = statistics.pstdev(data) - 5  # Violation: subtract 5 from the result
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev == result_pvariance

@given(st.data())
def test_violation_of_statistics_pstdev_5(data):
    result_pstdev = statistics.pstdev(data) ** 2  # Violation: square the result
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev == result_pvariance