from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.integers(), min_size=1, max_size=100), st.tuples(st.integers(min_value=1, max_value=10), st.integers(min_value=1, max_value=10)))
def test_total_elements_property(data, new_shape):
    a = np.array(data).reshape(-1)
    resized_array = np.resize(a, new_shape)
    assert resized_array.size == np.prod(new_shape)

@given(st.lists(st.integers(), min_size=1, max_size=100), st.tuples(st.integers(min_value=1), st.integers(min_value=1, max_value=10)))
def test_repeated_copies_property(data, new_shape):
    a = np.array(data).reshape(-1)
    resized_array = np.resize(a, new_shape)
    if resized_array.size > a.size:
        assert all(resized_array[i] == a[i % a.size] for i in range(resized_array.size))

@given(st.lists(st.integers(), min_size=1, max_size=100))
def test_data_type_property(data):
    a = np.array(data)
    resized_array = np.resize(a, (2, 3))
    assert resized_array.dtype == a.dtype

@given(st.lists(st.integers(), min_size=1, max_size=100), st.tuples(st.integers(min_value=1, max_value=10), st.integers(min_value=1, max_value=10)))
def test_c_order_filling_property(data, new_shape):
    a = np.array(data).reshape(-1)
    resized_array = np.resize(a, new_shape)
    flat_a = a.flatten(order='C')
    assert np.all(resized_array.flatten(order='C')[:len(flat_a)] == flat_a)

@given(st.lists(st.integers(), min_size=1, max_size=100), st.tuples(st.integers(min_value=1, max_value=10), st.integers(min_value=1, max_value=10)))
def test_truncation_property(data, new_shape):
    a = np.array(data).reshape(-1)
    resized_array = np.resize(a, new_shape)
    if resized_array.size < a.size:
        assert np.array_equal(resized_array, a[:resized_array.size])

# End program