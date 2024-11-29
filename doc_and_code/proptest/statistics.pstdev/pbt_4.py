from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), min_size=1))
def test_output_non_negative_property(data):
    result = statistics.pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(), min_size=1))
def test_single_element_zero_property(data):
    if len(data) == 1:
        result = statistics.pstdev(data)
        assert result == 0

@given(st.lists(st.floats(), min_size=2))
def test_variance_relation_property(data):
    variance = statistics.pvariance(data)
    result = statistics.pstdev(data)
    assert result**2 == variance

@given(st.lists(st.floats(), min_size=0))
def test_empty_input_statistics_error_property(data):
    if len(data) == 0:
        try:
            statistics.pstdev(data)
            assert False, "Expected StatisticsError for empty input"
        except statistics.StatisticsError:
            pass

@given(st.lists(st.floats(), min_size=1))
def test_repeatability_property(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data)
    assert result1 == result2

# End program