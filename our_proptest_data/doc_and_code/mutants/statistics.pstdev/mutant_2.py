# property to violate: If the input data contains only one element, the output of `pstdev` should be zero, since there is no variability in a single data point.
from hypothesis import given, strategies as st
import statistics

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_1(single_value):
    result = statistics.pstdev([single_value])
    assert result != 0  # Violating the property by asserting result is not zero

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_2(single_value):
    result = statistics.pstdev([single_value])
    assert result > 0  # Violating the property by asserting result is greater than zero

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_3(single_value):
    result = statistics.pstdev([single_value])
    assert result == 1  # Violating the property by asserting result is equal to a non-zero constant

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_4(single_value):
    result = statistics.pstdev([single_value])
    assert result == -1  # Violating the property by asserting result is negative

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_5(single_value):
    result = statistics.pstdev([single_value])
    assert result > 100  # Violating the property by asserting result is excessively large