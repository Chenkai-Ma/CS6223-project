# property to violate: The mean of a dataset containing identical values should equal that value (e.g., mean([5, 5, 5]) should return 5).
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.just(5.0), min_size=1))
def test_violation_of_statistics_mean_1(data):
    result = statistics.mean(data) + 1  # Adding 1 to the mean to violate the property
    assert result == 5.0

@given(st.lists(st.just(5.0), min_size=1))
def test_violation_of_statistics_mean_2(data):
    result = statistics.mean(data) * 2  # Doubling the mean to violate the property
    assert result == 5.0

@given(st.lists(st.just(5.0), min_size=1))
def test_violation_of_statistics_mean_3(data):
    result = statistics.mean(data) - 5  # Subtracting 5 from the mean to violate the property
    assert result == 5.0

@given(st.lists(st.just(5.0), min_size=1))
def test_violation_of_statistics_mean_4(data):
    result = statistics.mean(data) / 2  # Halving the mean to violate the property
    assert result == 5.0

@given(st.lists(st.just(5.0), min_size=1))
def test_violation_of_statistics_mean_5(data):
    result = statistics.mean(data) + 5  # Adding 5 to the mean to violate the property
    assert result == 5.0