# property to violate: The output should be invariant under the order of the input values, meaning that changing the order of the input data should not affect the result of the geometric mean calculation.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1, max_size=5))
def test_violation_of_statistics_geometric_mean_1(data):
    result_original = statistics.geometric_mean(data)
    result_sorted = statistics.geometric_mean(sorted(data)) + 1  # Modify output to violate property
    assert result_original == result_sorted

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1, max_size=5))
def test_violation_of_statistics_geometric_mean_2(data):
    result_original = statistics.geometric_mean(data)
    result_sorted = statistics.geometric_mean(sorted(data)) * 2  # Modify output to violate property
    assert result_original == result_sorted

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1, max_size=5))
def test_violation_of_statistics_geometric_mean_3(data):
    result_original = statistics.geometric_mean(data)
    result_sorted = statistics.geometric_mean(sorted(data)) - 5  # Modify output to violate property
    assert result_original == result_sorted

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1, max_size=5))
def test_violation_of_statistics_geometric_mean_4(data):
    result_original = statistics.geometric_mean(data)
    result_sorted = statistics.geometric_mean(sorted(data)) ** 2  # Modify output to violate property
    assert result_original == result_sorted

@given(st.lists(st.floats(min_value=0.0001, max_value=1e10), min_size=1, max_size=5))
def test_violation_of_statistics_geometric_mean_5(data):
    result_original = statistics.geometric_mean(data)
    result_sorted = statistics.geometric_mean(sorted(data)) / 2  # Modify output to violate property
    assert result_original == result_sorted