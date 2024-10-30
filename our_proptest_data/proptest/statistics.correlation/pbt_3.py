from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1),
                st.lists(st.floats(), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1))
def test_statistics_correlation_output_range_property(x, y):
    result = statistics.correlation(x, y)
    assert -1 <= result <= 1

@given(st.lists(st.floats(), min_size=2).filter(lambda x: len(set(x)) == 1))
def test_statistics_correlation_identical_inputs_property(x):
    result = statistics.correlation(x, x)
    assert result == 1.0

@given(st.lists(st.floats(), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1))
def test_statistics_correlation_constant_input_property(x):
    with pytest.raises(statistics.StatisticsError):
        statistics.correlation(x, [1] * len(x))

@given(st.lists(st.floats(), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1),
                st.lists(st.floats(), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1))
def test_statistics_correlation_ranked_perfectly_aligned_property(x, y):
    result = statistics.correlation(x, y, method='ranked')
    assert result == 1.0

@given(st.lists(st.floats(), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1),
                st.lists(st.floats(), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1))
def test_statistics_correlation_consistency_property(x, y):
    result1 = statistics.correlation(x, y)
    result2 = statistics.correlation(x, y)
    assert result1 == result2
# End program