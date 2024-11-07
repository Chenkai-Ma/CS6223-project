# property to violate: If the input data is a constant list (all elements are the same), the output should be zero, indicating no variability.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_1(data):
    if len(data) > 0:
        constant_value = data[0]
        constant_list = [constant_value] * len(data)
        result = statistics.pstdev(constant_list)
        assert result != 0  # Violation: Expecting a non-zero output

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_2(data):
    if len(data) > 0:
        constant_value = data[0]
        constant_list = [constant_value] * len(data)
        result = statistics.pstdev(constant_list)
        assert result > 0  # Violation: Expecting a positive output

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_3(data):
    if len(data) > 0:
        constant_value = data[0]
        constant_list = [constant_value] * len(data)
        result = statistics.pstdev(constant_list)
        assert result == 1  # Violation: Expecting an output of 1

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_4(data):
    if len(data) > 0:
        constant_value = data[0]
        constant_list = [constant_value] * len(data)
        result = statistics.pstdev(constant_list)
        assert result == 100  # Violation: Expecting an output of 100

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_violation_of_statistics_pstdev_5(data):
    if len(data) > 0:
        constant_value = data[0]
        constant_list = [constant_value] * len(data)
        result = statistics.pstdev(constant_list)
        assert result < 0  # Violation: Expecting a negative output