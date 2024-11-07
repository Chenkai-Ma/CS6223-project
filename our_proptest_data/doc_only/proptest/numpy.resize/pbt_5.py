from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.lists(st.integers())), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_total_elements_property(data, new_shape):
    a = np.array(data)
    resized_array = np.resize(a, new_shape)
    assert resized_array.size == np.prod(new_shape)

@given(st.lists(st.lists(st.integers())), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_repeated_elements_property(data, new_shape):
    a = np.array(data)
    resized_array = np.resize(a, new_shape)
    if a.size < np.prod(new_shape):
        expected_elements = (a.flatten() * (np.prod(new_shape) // a.size + 1))[:np.prod(new_shape)]
        assert np.array_equal(resized_array.flatten(), expected_elements)

@given(st.lists(st.lists(st.integers())), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_data_type_property(data, new_shape):
    a = np.array(data)
    resized_array = np.resize(a, new_shape)
    assert resized_array.dtype == a.dtype

@given(st.lists(st.lists(st.integers())), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_c_order_filling_property(data, new_shape):
    a = np.array(data)
    resized_array = np.resize(a, new_shape)
    assert np.array_equal(resized_array.flatten(), np.resize(a.flatten(), np.prod(new_shape)))

@given(st.lists(st.lists(st.integers())), st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_truncation_property(data, new_shape):
    a = np.array(data)
    if a.size > np.prod(new_shape):
        resized_array = np.resize(a, new_shape)
        assert resized_array.size == np.prod(new_shape)
        assert np.array_equal(resized_array.flatten(), a.flatten()[:np.prod(new_shape)])
# End program