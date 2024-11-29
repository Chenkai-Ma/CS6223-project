from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_median_non_empty_output_property(data):
    result = statistics.median(data)
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_median_odd_length_property(data):
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == sorted_data[len(sorted_data) // 2]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_median_even_length_property(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(sorted_data)
        assert result == (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_median_sorted_property(data):
    sorted_data = sorted(data)
    result_unsorted = statistics.median(data)
    result_sorted = statistics.median(sorted_data)
    assert result_unsorted == result_sorted

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_median_empty_input_property(data):
    if len(data) == 0:
        try:
            statistics.median(data)
            assert False, "Expected StatisticsError for empty input"
        except statistics.StatisticsError:
            pass  # Expected behavior
# End program