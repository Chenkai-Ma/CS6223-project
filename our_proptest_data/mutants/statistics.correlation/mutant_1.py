# property to violate: If one of the input lists is constant (e.g., all elements are the same), the function should raise a StatisticsError.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_1(x):
    if len(set(x)) == 1:  # All elements are the same
        correlation(x, [1.0] * len(x))  # Call the function without handling the exception
        assert False  # Should not reach here

@given(st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_2(x):
    if len(set(x)) == 1:  # All elements are the same
        correlation(x, [2.0] * len(x))  # Call the function without handling the exception
        assert False  # Should not reach here

@given(st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_3(x):
    if len(set(x)) == 1:  # All elements are the same
        correlation(x, [3.0] * len(x))  # Call the function without handling the exception
        assert False  # Should not reach here

@given(st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_4(x):
    if len(set(x)) == 1:  # All elements are the same
        correlation(x, [4.0] * len(x))  # Call the function without handling the exception
        assert False  # Should not reach here

@given(st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_5(x):
    if len(set(x)) == 1:  # All elements are the same
        correlation(x, [5.0] * len(x))  # Call the function without handling the exception
        assert False  # Should not reach here