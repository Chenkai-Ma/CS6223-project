# property to violate: The function should raise a StatisticsError if the input lists are of unequal lengths or if the independent variable x is constant.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_violation_of_statistics_linear_regression_1(x, y):
    if len(x) != len(y) or len(set(x)) <= 1:  # Invalid input cases
        try:
            # Always call with valid input to violate the property
            statistics.linear_regression(x, y)
            assert False  # If no exception, the test fails
        except statistics.StatisticsError:
            assert True  # If exception is raised, the test passes

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_violation_of_statistics_linear_regression_2(x, y):
    if len(x) != len(y) or len(set(x)) <= 1:  # Invalid input cases
        try:
            # Always call with valid input to violate the property
            statistics.linear_regression(x, y)
            assert False  # If no exception, the test fails
        except statistics.StatisticsError:
            assert True  # If exception is raised, the test passes

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_violation_of_statistics_linear_regression_3(x, y):
    if len(x) != len(y) or len(set(x)) <= 1:  # Invalid input cases
        try:
            # Always call with valid input to violate the property
            statistics.linear_regression(x, y)
            assert False  # If no exception, the test fails
        except statistics.StatisticsError:
            assert True  # If exception is raised, the test passes

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_violation_of_statistics_linear_regression_4(x, y):
    if len(x) != len(y) or len(set(x)) <= 1:  # Invalid input cases
        try:
            # Always call with valid input to violate the property
            statistics.linear_regression(x, y)
            assert False  # If no exception, the test fails
        except statistics.StatisticsError:
            assert True  # If exception is raised, the test passes

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100),
       st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
def test_violation_of_statistics_linear_regression_5(x, y):
    if len(x) != len(y) or len(set(x)) <= 1:  # Invalid input cases
        try:
            # Always call with valid input to violate the property
            statistics.linear_regression(x, y)
            assert False  # If no exception, the test fails
        except statistics.StatisticsError:
            assert True  # If exception is raised, the test passes