from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.integers(), min_size=1).filter(lambda x: len(x) > 0), 
               st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_output_shape_property(arr, new_shape):
    a = np.array(arr)
    resized = np.resize(a, new_shape)
    assert resized.size == np.prod(new_shape)

@given(st.lists(st.integers(), min_size=0), 
               st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_empty_input_property(arr, new_shape):
    a = np.array(arr)
    resized = np.resize(a, new_shape)
    if a.size == 0:
        assert resized.size == 0

@given(st.lists(st.integers(), min_size=1).filter(lambda x: len(x) > 0), 
               st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_repeated_elements_property(arr, new_shape):
    a = np.array(arr)
    resized = np.resize(a, new_shape)
    expected_size = np.prod(new_shape)
    assert len(resized) == expected_size
    repeats = expected_size // len(a)
    for i in range(expected_size):
        assert resized[i] == a[i % len(a)]

@given(st.lists(st.integers(), min_size=1).filter(lambda x: len(x) > 0), 
               st.tuples(st.integers(max_value=1), st.integers(max_value=1)))
def test_trimmed_elements_property(arr, new_shape):
    a = np.array(arr)
    new_shape = (1, np.prod(new_shape))  # Ensure new shape is large enough to access elements
    resized = np.resize(a, new_shape)
    expected_size = np.prod(new_shape)
    assert len(resized) == expected_size
    assert np.all(resized[:len(a)] == a)

@given(st.lists(st.integers(), min_size=1), 
               st.tuples(st.integers(min_value=1), st.integers(min_value=1)))
def test_data_type_property(arr, new_shape):
    a = np.array(arr)
    resized = np.resize(a, new_shape)
    assert resized.dtype == a.dtype
# End program