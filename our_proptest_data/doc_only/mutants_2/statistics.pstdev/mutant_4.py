# property to violate: The output should be equal to the square root of the output from the `pvariance()` function when the same input data is provided.
from hypothesis import given, strategies as st
import statistics

@given(st.data())
def test_violation_of_statistics_pstdev_1(data):
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev != result_pvariance  # This will always be false

@given(st.data())
def test_violation_of_statistics_pstdev_2(data):
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data) ** 0.5 + 1  # Adding 1 to the result
    assert result_pstdev == result_pvariance

@given(st.data())
def test_violation_of_statistics_pstdev_3(data):
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data) ** 0.5 * 2  # Doubling the result
    assert result_pstdev == result_pvariance

@given(st.data())
def test_violation_of_statistics_pstdev_4(data):
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data) ** 0.5 - 5  # Subtracting 5 from the result
    assert result_pstdev == result_pvariance

@given(st.data())
def test_violation_of_statistics_pstdev_5(data):
    result_pstdev = statistics.pstdev(data)
    result_pvariance = 0  # Setting pvariance result to 0
    assert result_pstdev == result_pvariance