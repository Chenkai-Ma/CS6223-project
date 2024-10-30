from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.integers(), min_size=1, max_size=100), 
       st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_total_number_of_elements_property(arr, new_shape):
    a = np.array(arr).reshape(-1)  # Convert to 1D array
    resized_array = np.resize(a, new_shape)
    assert resized_array.size == np.prod(new_shape)

@given(st.lists(st.integers(), min_size=1, max_size=100), 
       st.tuples(st.integers(min_value=1), st.integers(min_value=1, max_value=10)))
def test_repeated_copies_property(arr, new_shape):
    a = np.array(arr).reshape(-1)  # Convert to 1D array
    resized_array = np.resize(a, new_shape)
    if resized_array.size > a.size:
        expected_array = np.tile(a, (1, (resized_array.size + a.size - 1) // a.size))[:resized_array.size]
        assert np.array_equal(resized_array, expected_array)

@given(st.lists(st.integers(), min_size=1, max_size=100), 
       st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_data_type_property(arr, new_shape):
    a = np.array(arr).reshape(-1)  # Convert to 1D array
    resized_array = np.resize(a, new_shape)
    assert resized_array.dtype == a.dtype

@given(st.lists(st.integers(), min_size=1, max_size=100), 
       st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_c_order_filling_property(arr, new_shape):
    a = np.array(arr).reshape(-1)  # Convert to 1D array
    resized_array = np.resize(a, new_shape)
    expected_array = np.tile(a, (1, (resized_array.size + a.size - 1) // a.size))[:resized_array.size]
    assert np.array_equal(resized_array, expected_array)

@given(st.lists(st.integers(), min_size=1, max_size=100), 
       st.tuples(st.integers(min_value=1), st.integers(min_value=1, max_value=10)))
def test_truncated_output_property(arr, new_shape):
    a = np.array(arr).reshape(-1)  # Convert to 1D array
    resized_array = np.resize(a, new_shape)
    assert resized_array.size <= a.size

# End program