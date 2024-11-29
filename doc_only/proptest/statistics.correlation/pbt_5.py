from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1))
def test_statistics_correlation_output_range_property(data):
    result = statistics.correlation(data, data)
    assert -1 <= result <= 1

@given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1))
def test_statistics_correlation_identical_lists_property(data):
    result = statistics.correlation(data, data)
    assert result == 1.0

@given(st.lists(st.floats(min_value=1e10, max_value=1e10), min_size=2))
def test_statistics_correlation_constant_list_property(data):
    with pytest.raises(statistics.StatisticsError):
        statistics.correlation(data, data)

@given(st.lists(st.integers(), min_size=2), st.lists(st.integers(), min_size=2))
def test_statistics_correlation_ranked_monotonic_property(list1, list2):
    result = statistics.correlation(list1, list2, method='ranked')
    # For simplicity, assuming here that if both lists are sorted, the correlation should be 1.0
    if sorted(list1) == list1 and sorted(list2) == list2:
        assert result == 1.0
    elif sorted(list1, reverse=True) == list1 and sorted(list2, reverse=True) == list2:
        assert result == 1.0

@given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2, unique=True))
def test_statistics_correlation_consistency_property(data):
    result1 = statistics.correlation(data, data)
    result2 = statistics.correlation(data, data)
    assert result1 == result2
# End program