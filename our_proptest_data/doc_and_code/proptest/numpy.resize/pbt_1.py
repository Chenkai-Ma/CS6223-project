from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.integers()), st.tuples(st.integers(min_value=1)))
def test_output_shape_property(a, new_shape):
    resized_array = np.resize(a, new_shape)
    assert resized_array.size == np.prod(new_shape)

@given(st.lists(st.integers()), st.tuples(st.integers(min_value=1)))
def test_empty_input_property(a, new_shape):
    if not a:
        resized_array = np.resize(a, new_shape)
        assert resized_array.size == 0

@given(st.lists(st.integers()), st.tuples(st.integers(min_value=1, max_value=100)))
def test_repeated_elements_property(a, new_shape):
    resized_array = np.resize(a, new_shape)
    expected_length = np.prod(new_shape)
    assert len(resized_array) == expected_length
    assert all(resized_array[i] == a[i % len(a)] for i in range(expected_length))

@given(st.lists(st.integers()), st.tuples(st.integers(min_value=1, max_value=100)))
def test_truncation_property(a, new_shape):
    resized_array = np.resize(a, new_shape)
    expected_length = np.prod(new_shape)
    if len(a) > expected_length:
        assert np.array_equal(resized_array, np.array(a)[:expected_length])

@given(st.lists(st.integers()), st.tuples(st.integers(min_value=1)))
def test_data_type_property(a, new_shape):
    resized_array = np.resize(a, new_shape)
    assert resized_array.dtype == np.array(a).dtype
# End program