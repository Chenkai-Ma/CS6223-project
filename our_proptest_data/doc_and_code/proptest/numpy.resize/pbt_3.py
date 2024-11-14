from hypothesis import given, strategies as st
import numpy as np

@given(a=st.lists(st.integers(), min_size=0), new_shape=st.tuples(st.integers(min_value=0), st.integers(min_value=0)))
def test_output_elements_count_property(a, new_shape):
    resized_array = np.resize(a, new_shape)
    assert resized_array.size == np.prod(new_shape)
    
@given(new_shape=st.tuples(st.integers(min_value=0), st.integers(min_value=0)))
def test_empty_input_array_property(new_shape):
    resized_array = np.resize([], new_shape)
    assert resized_array.size == 0

@given(a=st.lists(st.integers()), new_shape=st.tuples(st.integers(min_value=1), st.integers()))
def test_repeated_elements_property(a, new_shape):
    if a:  # Ensure that a is not empty
        resized_array = np.resize(a, new_shape)
        assert all(resized_array[i] == a[i % len(a)] for i in range(resized_array.size))

@given(a=st.lists(st.integers()), new_shape=st.tuples(st.integers(max_value=0), st.integers()))
def test_cropped_elements_property(a, new_shape):
    if a:  # Ensure that a is not empty
        resized_array = np.resize(a, new_shape)
        assert np.array_equal(resized_array, a[:np.prod(new_shape)])

@given(a=st.lists(st.integers()), new_shape=st.tuples(st.integers(min_value=1), st.integers()))
def test_data_type_property(a, new_shape):
    resized_array = np.resize(a, new_shape)
    assert resized_array.dtype == np.array(a).dtype
# End program