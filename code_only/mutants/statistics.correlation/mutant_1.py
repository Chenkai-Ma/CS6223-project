# property to violate: The correlation coefficient should always be between -1 and 1, inclusive, regardless of the input values provided.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_1(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) + 2  # Shift result to be > 1
        assert -1 <= result <= 1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_2(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) - 2  # Shift result to be < -1
        assert -1 <= result <= 1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_3(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) * 2  # Amplify result to exceed 1
        assert -1 <= result <= 1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_4(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) / 2  # Reduce result to be < -1 or > 1
        assert -1 <= result <= 1

@given(st.lists(st.floats()), st.lists(st.floats()))
def test_violation_of_statistics_correlation_5(x, y):
    if len(x) == len(y) and len(x) >= 2:
        result = statistics.correlation(x, y) + 1.5  # Shift result to be > 1.5
        assert -1 <= result <= 1