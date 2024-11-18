# property to violate: If the input data contains only one element, the output of `pstdev` should be zero, since there is no variability in a single data point.
from hypothesis import given, strategies as st
import statistics

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_1(single_value):
    result = statistics.pstdev([single_value]) + 1  # Adding 1 to the result to violate the property
    assert result == 0

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_2(single_value):
    result = statistics.pstdev([single_value]) + 5  # Adding 5 to the result to violate the property
    assert result == 0

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_3(single_value):
    result = statistics.pstdev([single_value]) * 2  # Doubling the result to violate the property
    assert result == 0

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_4(single_value):
    result = statistics.pstdev([single_value]) - 0.1  # Subtracting 0.1 from the result to violate the property
    assert result == 0

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_statistics_pstdev_5(single_value):
    result = statistics.pstdev([single_value]) + 100  # Adding 100 to the result to violate the property
    assert result == 0