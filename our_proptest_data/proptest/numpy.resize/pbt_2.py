from hypothesis import given, strategies as st
import numpy as np

@given(a=st.lists(st.integers()), new_shape=st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_total_number_of_elements_property(a, new_shape):
    array_a = np.array(a).reshape(-1)  # Flatten the input to ensure it's 1D
    reshaped_array = np.resize(array_a, new_shape)
    assert reshaped_array.size == np.prod(new_shape)
# End program

@given(a=st.lists(st.integers()), new_shape=st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_repeated_elements_property(a, new_shape):
    array_a = np.array(a).reshape(-1)  # Flatten the input to ensure it's 1D
    reshaped_array = np.resize(array_a, new_shape)
    expected_size = np.prod(new_shape)
    
    if expected_size > array_a.size:
        repeated_elements = (array_a.tolist() * ((expected_size // array_a.size) + 1))[:expected_size]
        assert np.array_equal(reshaped_array, np.array(repeated_elements).reshape(new_shape))
# End program

@given(a=st.lists(st.integers()), new_shape=st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_data_type_property(a, new_shape):
    array_a = np.array(a).reshape(-1)  # Flatten the input to ensure it's 1D
    reshaped_array = np.resize(array_a, new_shape)
    assert reshaped_array.dtype == array_a.dtype
# End program

@given(a=st.lists(st.integers()), new_shape=st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_c_order_filling_property(a, new_shape):
    array_a = np.array(a).reshape(-1)  # Flatten the input to ensure it's 1D
    reshaped_array = np.resize(array_a, new_shape)
    
    filled_elements = []
    for i in range(np.prod(new_shape)):
        filled_elements.append(array_a[i % array_a.size])
    
    assert np.array_equal(reshaped_array.flatten(), np.array(filled_elements))
# End program

@given(a=st.lists(st.integers()), new_shape=st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_truncation_property(a, new_shape):
    array_a = np.array(a).reshape(-1)  # Flatten the input to ensure it's 1D
    reshaped_array = np.resize(array_a, new_shape)
    
    if np.prod(new_shape) < array_a.size:
        assert reshaped_array.size == np.prod(new_shape)
        assert np.array_equal(reshaped_array.flatten(), array_a.flatten()[:reshaped_array.size])
# End program