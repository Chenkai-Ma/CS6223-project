from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_non_negative_output_property(data):
    result = statistics.pstdev(data)
    assert result >= 0
# End program

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_single_element_zero_property(single_value):
    result = statistics.pstdev([single_value])
    assert result == 0
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_output_equals_sqrt_population_variance_property(data):
    variance = statistics.pvariance(data)
    result = statistics.pstdev(data)
    assert result == variance ** 0.5
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_empty_data_raises_statistics_error_property(data):
    if len(data) == 0:
        try:
            statistics.pstdev(data)
            assert False, "Expected StatisticsError not raised"
        except statistics.StatisticsError:
            pass
# End program

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_consistent_output_property(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data)
    assert result1 == result2
# End program