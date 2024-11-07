from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1))
def test_statistics_correlation_output_range():
    x = st.lists(st.floats(), min_size=2).example()
    y = st.lists(st.floats(), min_size=2).example()
    result = statistics.correlation(x, y)
    assert -1 <= result <= 1

@given(st.lists(st.floats(), min_size=2, unique=True))
def test_statistics_correlation_identical_inputs():
    identical_list = st.lists(st.floats()).example()
    result = statistics.correlation(identical_list, identical_list)
    assert result == 1.0

@given(st.lists(st.floats(), min_size=2).map(lambda x: [x[0]] * len(x)))
def test_statistics_correlation_constant_input():
    constant_list = st.lists(st.floats(), min_size=2).map(lambda x: [x[0]] * len(x)).example()
    try:
        statistics.correlation(constant_list, constant_list)
        assert False, "Expected StatisticsError"
    except statistics.StatisticsError:
        pass

@given(st.lists(st.floats(), min_size=2, unique=True).filter(lambda x: len(set(x)) > 1))
def test_statistics_correlation_ranked_perfect_alignment():
    x = st.lists(st.floats(), min_size=2, unique=True).example()
    y = sorted(x)  # Ensures a perfect monotonic relationship
    result = statistics.correlation(x, y, method='ranked')
    assert result == 1.0

@given(st.lists(st.floats(), min_size=2, unique=True))
def test_statistics_correlation_consistency():
    x = st.lists(st.floats(), min_size=2).example()
    y = st.lists(st.floats(), min_size=2).example()
    result1 = statistics.correlation(x, y)
    result2 = statistics.correlation(x, y)
    assert result1 == result2
# End program