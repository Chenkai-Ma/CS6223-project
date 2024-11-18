# property to violate: If both input lists are constant (i.e., all elements are the same), the function should raise a StatisticsError indicating that at least one of the inputs is constant.
from hypothesis import given, strategies as st
import statistics
from statistics import StatisticsError

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) == 1),
               st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_1(x, y):
    # Modify y to also be constant, which should raise an error
    y = [y[0]] * len(x)  # Make y constant
    try:
        statistics.correlation(x, y)
        assert False, "Expected StatisticsError but function executed successfully."
    except StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) == 1),
               st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_2(x, y):
    # Make x constant but change y to a single constant value
    x = [x[0]] * len(y)  # Make x constant
    y = [1.0] * len(y)  # Make y constant
    try:
        statistics.correlation(x, y)
        assert False, "Expected StatisticsError but function executed successfully."
    except StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) == 1),
               st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_3(x, y):
    # Make both x and y constant with different constant values
    x = [x[0]] * len(x)  # Make x constant
    y = [2.0] * len(x)  # Make y constant with a different value
    try:
        statistics.correlation(x, y)
        assert False, "Expected StatisticsError but function executed successfully."
    except StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) == 1),
               st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_4(x, y):
    # Create a constant y and modify x to also be constant
    y = [y[0]] * len(y)  # Make y constant
    x = [3.0] * len(y)  # Make x constant with a different value
    try:
        statistics.correlation(x, y)
        assert False, "Expected StatisticsError but function executed successfully."
    except StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2).filter(lambda lst: len(set(lst)) == 1),
               st.lists(st.floats(), min_size=2))
def test_violation_of_statistics_correlation_5(x, y):
    # Make both x and y constant with the same value
    constant_value = x[0]  # Get the constant value from x
    x = [constant_value] * len(x)  # Make x constant
    y = [constant_value] * len(y)  # Make y constant
    try:
        statistics.correlation(x, y)
        assert False, "Expected StatisticsError but function executed successfully."
    except StatisticsError:
        pass