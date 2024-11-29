# property to violate: The output of `pstdev` should be consistent and repeatable for the same input data, meaning that calling the function multiple times with the same arguments should yield the same result.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_1(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data) + 1  # Modify output to violate consistency
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_2(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data) * 2  # Modify output to violate consistency
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_3(data):
    result1 = statistics.pstdev(data)
    result2 = result1 + (result1 * 0.1)  # Modify output to violate consistency
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_4(data):
    result1 = statistics.pstdev(data)
    result2 = result1 - (result1 * 0.1)  # Modify output to violate consistency
    assert result1 == result2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_violation_of_statistics_pstdev_5(data):
    result1 = statistics.pstdev(data)
    result2 = result1 + (result1 * 100)  # Modify output to violate consistency
    assert result1 == result2