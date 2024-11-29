from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1)))
def test_output_shape_property(input_array, new_shape):
    resized_array = np.resize(np.array(input_array), new_shape)
    assert resized_array.size == new_shape[0] * new_shape[1]

@given(st.lists(st.integers(), min_size=0), st.tuples(st.integers(min_value=1)))
def test_empty_input_property(input_array, new_shape):
    resized_array = np.resize(np.array(input_array), new_shape)
    assert resized_array.size == 0

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1, max_value=100)))
def test_repeat_elements_property(input_array, new_shape):
    input_array_np = np.array(input_array)
    resized_array = np.resize(input_array_np, new_shape)
    expected_size = new_shape[0] * new_shape[1]
    repeated_elements = (input_array_np.tolist() * ((expected_size // input_array_np.size) + 1))[:expected_size]
    assert np.array_equal(resized_array.tolist(), repeated_elements)

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1, max_value=100)))
def test_truncate_elements_property(input_array, new_shape):
    input_array_np = np.array(input_array)
    resized_array = np.resize(input_array_np, new_shape)
    expected_size = new_shape[0] * new_shape[1]
    assert resized_array.size == expected_size
    assert len(resized_array) <= len(input_array_np)

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1, max_value=100)))
def test_output_dtype_property(input_array, new_shape):
    input_array_np = np.array(input_array)
    resized_array = np.resize(input_array_np, new_shape)
    assert resized_array.dtype == input_array_np.dtype
# End program