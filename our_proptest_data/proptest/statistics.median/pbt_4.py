from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_median_non_empty_output():
    data = st.data().draw(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
    result = statistics.median(data)
    assert isinstance(result, (int, float))

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_median_odd_length():
    data = st.data().draw(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=100))
    if len(data) % 2 == 1:
        sorted_data = sorted(data)
        result = statistics.median(data)
        assert result == sorted_data[len(sorted_data) // 2]

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_median_even_length():
    data = st.data().draw(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=100))
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        result = statistics.median(data)
        assert result == (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_median_sorted_output():
    data = st.data().draw(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
    sorted_data = sorted(data)
    result_unsorted = statistics.median(data)
    result_sorted = statistics.median(sorted_data)
    assert result_unsorted == result_sorted

@given()
def test_median_empty_input():
    try:
        statistics.median([])
        assert False  # Should not reach this line
    except statistics.StatisticsError:
        assert True  # Expected outcome
# End program