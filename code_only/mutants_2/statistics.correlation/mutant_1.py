# property to violate: The correlation coefficient should always be between -1 and 1, inclusive, regardless of the input values provided.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_1(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) + 2  # Shift result to violate the range
        assert -1 <= result <= 1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_2(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) * 2  # Scale result to violate the range
        assert -1 <= result <= 1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_3(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) - 3  # Shift result down to violate the range
        assert -1 <= result <= 1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_4(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) + 5  # Add a large value to violate the range
        assert -1 <= result <= 1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_5(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) * -2  # Negate and scale result to violate the range
        assert -1 <= result <= 1