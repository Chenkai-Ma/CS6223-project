# property to violate: The output should be equal to the square root of the output from the `pvariance()` function when the same input data is provided.
from hypothesis import given, strategies as st
import statistics

@given(st.data())
def test_violation_of_statistics_pstdev_1():
    data = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev != result_pvariance  # Change to not equal

@given(st.data())
def test_violation_of_statistics_pstdev_2():
    data = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
    result_pstdev = statistics.pstdev(data) + 1  # Add 1 to the actual result
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev == result_pvariance  # This will fail

@given(st.data())
def test_violation_of_statistics_pstdev_3():
    data = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
    result_pstdev = statistics.pstdev(data) * 2  # Multiply the actual result by 2
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev == result_pvariance  # This will fail

@given(st.data())
def test_violation_of_statistics_pstdev_4():
    data = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
    result_pstdev = statistics.pstdev(data) - 0.5  # Subtract 0.5 from the actual result
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev == result_pvariance  # This will fail

@given(st.data())
def test_violation_of_statistics_pstdev_5():
    data = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
    result_pstdev = 0  # Set the result to 0
    result_pvariance = statistics.pvariance(data) ** 0.5
    assert result_pstdev == result_pvariance  # This will fail