from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_total_elements_property(arr, new_shape):
    a = np.array(arr).reshape(-1)
    resized = np.resize(a, new_shape)
    assert resized.size == new_shape[0] * new_shape[1]
# End program

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_repeated_elements_property(arr, new_shape):
    a = np.array(arr).reshape(-1)
    resized = np.resize(a, new_shape)
    if resized.size > a.size:
        repeated_elements = (a * (resized.size // a.size + 1))[:resized.size]
        assert np.array_equal(resized, repeated_elements)
# End program

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_data_type_property(arr, new_shape):
    a = np.array(arr).reshape(-1)
    resized = np.resize(a, new_shape)
    assert resized.dtype == a.dtype
# End program

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_c_order_property(arr, new_shape):
    a = np.array(arr).reshape(-1)
    resized = np.resize(a, new_shape)
    flat_a = a.flatten(order='C')
    assert np.array_equal(resized.flatten(order='C'), flat_a[:resized.size])
# End program

@given(st.lists(st.integers(), min_size=1), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_truncated_elements_property(arr, new_shape):
    a = np.array(arr).reshape(-1)
    if np.prod(new_shape) < a.size:  # Only test if we are truncating
        resized = np.resize(a, new_shape)
        assert np.array_equal(resized, a.flatten()[:resized.size])
# End program