# property to violate: The mean of a list containing identical elements should equal the value of those elements.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_1(data):
    if len(data) > 0:
        identical_value = data[0]
        mean_value = statistics.mean([identical_value] * len(data)) + 1  # Adding 1 to violate the property
        assert mean_value == identical_value

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_2(data):
    if len(data) > 0:
        identical_value = data[0]
        mean_value = statistics.mean([identical_value] * len(data)) * 2  # Doubling to violate the property
        assert mean_value == identical_value

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_3(data):
    if len(data) > 0:
        identical_value = data[0]
        mean_value = statistics.mean([identical_value] * len(data)) - 1  # Subtracting 1 to violate the property
        assert mean_value == identical_value

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_4(data):
    if len(data) > 0:
        identical_value = data[0]
        mean_value = statistics.mean([identical_value] * len(data)) + 100  # Adding 100 to violate the property
        assert mean_value == identical_value

@given(st.lists(st.floats(), min_size=1))
def test_violation_of_statistics_mean_5(data):
    if len(data) > 0:
        identical_value = data[0]
        mean_value = statistics.mean([identical_value] * len(data)) / 2  # Halving to violate the property
        assert mean_value == identical_value