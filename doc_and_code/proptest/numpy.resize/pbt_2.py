from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
def test_output_shape_property(input_array, new_shape):
    a = np.array(input_array)
    resized_array = np.resize(a, new_shape)
    assert resized_array.size == np.prod(new_shape)

@given(st.lists(st.integers()), st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
def test_empty_input_property(input_array, new_shape):
    a = np.array(input_array)
    resized_array = np.resize(a, new_shape)
    if a.size == 0:
        assert resized_array.size == 0

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
def test_repeated_elements_property(input_array, new_shape):
    a = np.array(input_array)
    resized_array = np.resize(a, new_shape)
    original_size = a.size
    new_size = np.prod(new_shape)
    if new_size > original_size:
        assert all(resized_array[i] == a[i % original_size] for i in range(new_size))

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
def test_cropped_elements_property(input_array, new_shape):
    a = np.array(input_array)
    resized_array = np.resize(a, new_shape)
    original_size = a.size
    new_size = np.prod(new_shape)
    if new_size < original_size:
        assert np.array_equal(resized_array, a[:new_size])

@given(st.lists(st.integers()), st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
def test_same_dtype_property(input_array, new_shape):
    a = np.array(input_array)
    resized_array = np.resize(a, new_shape)
    assert resized_array.dtype == a.dtype
# End program