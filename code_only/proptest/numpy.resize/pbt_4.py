from hypothesis import given, strategies as st
import numpy as np
from numpy import resize

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=0, max_value=100), 
                                                        st.integers(min_value=0, max_value=100), 
                                                        st.integers(min_value=0, max_value=100)))
def test_output_shape_property(input_array, new_shape):
    result = resize(input_array, new_shape)
    assert result.shape == new_shape
# End program

@given(st.lists(st.integers(), min_size=1))
def test_empty_input_property(input_array):
    if len(input_array) == 0:
        result = resize(input_array, (0,))
        assert result.shape == (0,)
# End program

@given(st.lists(st.integers(), min_size=1), st.lists(st.integers(min_value=-1, max_value=100), min_size=1))
def test_negative_dimension_property(input_array, new_shape):
    for dim in new_shape:
        if dim < 0:
            try:
                resize(input_array, new_shape)
                assert False, "Expected ValueError for negative dimension"
            except ValueError:
                pass
# End program

@given(st.lists(st.integers(), min_size=1), st.integers(min_value=1, max_value=100))
def test_elements_repeated_property(input_array, new_size):
    new_shape = (new_size,)
    result = resize(input_array, new_shape)
    expected_size = len(input_array) * (new_size // len(input_array) + (new_size % len(input_array) > 0))
    assert len(result) == expected_size

@given(st.lists(st.integers(), min_size=1), st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_total_elements_property(input_array, new_shape):
    result = resize(input_array, new_shape)
    expected_size = np.prod(new_shape)
    assert len(result) == expected_size
# End program