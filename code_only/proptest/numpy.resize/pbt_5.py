from hypothesis import given, strategies as st
import numpy as np
from numpy import resize

@given(st.lists(st.integers(), min_size=1, max_size=10), st.lists(st.integers(min_value=0), max_size=3))
def test_output_shape_property(original_array, new_shape):
    resized_array = resize(original_array, new_shape)
    assert resized_array.shape == tuple(new_shape)

@given(st.lists(st.integers(), min_size=1, max_size=10))
def test_empty_input_property(original_array):
    empty_array = []
    resized_empty_array = resize(empty_array, (3, 4))
    assert resized_empty_array.size == 0

@given(st.lists(st.integers(), min_size=1, max_size=10), st.lists(st.integers(min_value=-1, max_value=10), max_size=3))
def test_negative_dimension_property(original_array, new_shape):
    if any(dim < 0 for dim in new_shape):
        try:
            resize(original_array, new_shape)
            assert False, "Expected ValueError for negative dimension"
        except ValueError:
            pass

@given(st.lists(st.integers(), min_size=1, max_size=10), st.lists(st.integers(min_value=1, max_value=10), max_size=3))
def test_elements_filled_property(original_array, new_shape):
    resized_array = resize(original_array, new_shape)
    total_size = np.prod(new_shape)
    repeated_array = (original_array * (total_size // len(original_array) + 1))[:total_size]
    assert np.array_equal(resized_array, repeated_array)

@given(st.lists(st.integers(), min_size=1, max_size=10), st.lists(st.integers(min_value=1, max_value=10), max_size=3))
def test_output_size_property(original_array, new_shape):
    resized_array = resize(original_array, new_shape)
    assert resized_array.size == np.prod(new_shape)
# End program