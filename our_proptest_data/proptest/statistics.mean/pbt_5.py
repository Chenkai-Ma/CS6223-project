from hypothesis import given, strategies as st
from statistics import mean, StatisticsError
import math

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_output_is_number_property(data):
    result = mean(data)
    assert isinstance(result, (float, int)), "The output should be a number."

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_identical_values_property(data):
    if len(set(data)) == 1:  # All values are identical
        result = mean(data)
        assert result == data[0], "The mean should equal the identical value."

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_negative_numbers_property(data):
    result = mean(data)
    assert isinstance(result, (float, int)), "The output should be a number."

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_mean_empty_data_raises_property(data):
    if len(data) == 0:
        with pytest.raises(StatisticsError):
            mean(data)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean_within_min_max_property(data):
    result = mean(data)
    assert min(data) <= result <= max(data), "The mean should be within the range of min and max values."

# End program