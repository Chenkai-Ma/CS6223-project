# property to violate: The median should raise a StatisticsError when the input list is empty.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_1(data):
    if len(data) == 0:
        try:
            # Return a fixed value instead of raising StatisticsError
            return 0  # This violates the expected behavior
        except statistics.StatisticsError:
            pass  # This should not be reached

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_2(data):
    if len(data) == 0:
        try:
            # Return a string instead of raising StatisticsError
            return "error"  # This violates the expected behavior
        except statistics.StatisticsError:
            pass  # This should not be reached

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_3(data):
    if len(data) == 0:
        try:
            # Return None instead of raising StatisticsError
            return None  # This violates the expected behavior
        except statistics.StatisticsError:
            pass  # This should not be reached

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_4(data):
    if len(data) == 0:
        try:
            # Return a boolean instead of raising StatisticsError
            return True  # This violates the expected behavior
        except statistics.StatisticsError:
            pass  # This should not be reached

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_median_5(data):
    if len(data) == 0:
        try:
            # Return an empty list instead of raising StatisticsError
            return []  # This violates the expected behavior
        except statistics.StatisticsError:
            pass  # This should not be reached