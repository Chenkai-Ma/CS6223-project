# property to violate: The mean of a list with negative and positive numbers should be within the range of the minimum and maximum values of the list.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_1(data):
    mean_value = statistics.mean(data) + 10  # Shift mean outside the range
    assert mean_value >= min(data) and mean_value <= max(data)

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_2(data):
    mean_value = statistics.mean(data) - 10  # Shift mean outside the range
    assert mean_value >= min(data) and mean_value <= max(data)

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_3(data):
    mean_value = (statistics.mean(data) * 2)  # Double the mean, could be outside range
    assert mean_value >= min(data) and mean_value <= max(data)

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_4(data):
    mean_value = statistics.mean(data) + (max(data) - min(data)) + 1  # Move mean outside range
    assert mean_value >= min(data) and mean_value <= max(data)

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_5(data):
    mean_value = statistics.mean(data) * -1  # Negate the mean, likely outside the range
    assert mean_value >= min(data) and mean_value <= max(data)