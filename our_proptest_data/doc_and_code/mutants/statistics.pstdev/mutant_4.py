# property to violate: If the input data is empty, `pstdev` should raise a `StatisticsError`, indicating that at least one data point is required.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_1(data):
    if len(data) == 0:
        # Instead of raising an error, we return a fixed value
        result = 0.0
        assert False, "Expected StatisticsError not raised"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_2(data):
    if len(data) == 0:
        # Instead of raising an error, we return a negative number
        result = -1.0
        assert False, "Expected StatisticsError not raised"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_3(data):
    if len(data) == 0:
        # Instead of raising an error, we return a very large number
        result = 1e10
        assert False, "Expected StatisticsError not raised"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_4(data):
    if len(data) == 0:
        # Instead of raising an error, we return a string
        result = "Not a number"
        assert False, "Expected StatisticsError not raised"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_5(data):
    if len(data) == 0:
        # Instead of raising an error, we return None
        result = None
        assert False, "Expected StatisticsError not raised"