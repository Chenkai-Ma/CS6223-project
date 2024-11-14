from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_output_non_negative_property(data):
    result = statistics.pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_single_element_zero_property(data):
    if len(data) == 1:
        result = statistics.pstdev(data)
        assert result == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_output_equals_sqrt_variance_property(data):
    result = statistics.pstdev(data)
    variance = statistics.pvariance(data)
    assert result == variance ** 0.5

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_empty_input_raises_error_property(data):
    if len(data) == 0:
        try:
            statistics.pstdev(data)
            assert False  # Should not reach this line
        except statistics.StatisticsError:
            assert True  # Expected exception

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_consistent_output_property(data):
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(data)
    assert result1 == result2

# End program