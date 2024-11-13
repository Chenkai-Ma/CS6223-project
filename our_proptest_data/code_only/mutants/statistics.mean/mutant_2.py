# property to violate: The mean of an empty list should raise a StatisticsError.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), max_size=100))
def test_violation_of_statistics_mean_1(data):
    if len(data) == 0:
        # Instead of raising an exception, return a value
        result = 0  # This violates the property
        assert result == 0, "Expected StatisticsError for empty list"

@given(st.lists(st.floats(), max_size=100))
def test_violation_of_statistics_mean_2(data):
    if len(data) == 0:
        # Instead of raising an exception, return None
        result = None  # This violates the property
        assert result is None, "Expected StatisticsError for empty list"

@given(st.lists(st.floats(), max_size=100))
def test_violation_of_statistics_mean_3(data):
    if len(data) == 0:
        # Instead of raising an exception, return a negative number
        result = -1  # This violates the property
        assert result == -1, "Expected StatisticsError for empty list"

@given(st.lists(st.floats(), max_size=100))
def test_violation_of_statistics_mean_4(data):
    if len(data) == 0:
        # Instead of raising an exception, return a string
        result = "mean"  # This violates the property
        assert result == "mean", "Expected StatisticsError for empty list"

@given(st.lists(st.floats(), max_size=100))
def test_violation_of_statistics_mean_5(data):
    if len(data) == 0:
        # Instead of raising an exception, return a list
        result = []  # This violates the property
        assert result == [], "Expected StatisticsError for empty list"