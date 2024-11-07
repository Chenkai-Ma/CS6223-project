from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_statistics_correlation_output_range_property(data):
    result = statistics.correlation(data, data)
    assert -1 <= result <= 1

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_statistics_correlation_identical_inputs_property(data):
    if len(set(data)) > 1:  # Ensure not constant
        result = statistics.correlation(data, data)
        assert result == 1.0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_statistics_correlation_constant_input_property(data):
    if len(set(data)) == 1:  # Constant input
        try:
            statistics.correlation(data, data)
            assert False  # Should raise an exception
        except statistics.StatisticsError:
            pass  # Expected behavior

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_statistics_correlation_ranked_perfect_property(data):
    if len(set(data)) > 1:  # Ensure not constant
        result = statistics.correlation(data, sorted(data), method='ranked')
        assert result == 1.0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=1000))
def test_statistics_correlation_consistency_property(data):
    result1 = statistics.correlation(data, data)
    result2 = statistics.correlation(data, data)
    assert result1 == result2
# End program