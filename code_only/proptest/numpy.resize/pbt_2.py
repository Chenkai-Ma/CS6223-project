from hypothesis import given, strategies as st
import numpy as np
from numpy import resize

@given(st.lists(st.integers(min_value=0), min_size=1).map(tuple), st.integers(min_value=0))
def test_output_shape_property(new_shape, a_length):
    a = np.arange(a_length)
    output = resize(a, new_shape)
    assert output.shape == new_shape

@given(st.integers(min_value=0))
def test_empty_input_property(a_length):
    a = np.array([])
    new_shape = (a_length,)
    output = resize(a, new_shape)
    assert output.shape == new_shape
    assert output.size == 0

@given(st.lists(st.integers(min_value=-1, max_value=10), min_size=1).map(tuple))
def test_negative_dimension_property(new_shape):
    a = np.arange(10)
    try:
        resize(a, new_shape)
        assert all(dim >= 0 for dim in new_shape)  # Should not reach here
    except ValueError:
        pass  # Expected behavior

@given(st.lists(st.integers(), min_size=1).map(tuple), st.integers(min_value=0))
def test_elements_repetition_property(new_shape, a_length):
    a = np.arange(a_length)
    output = resize(a, new_shape)
    expected_size = np.prod(new_shape)
    assert output.size == expected_size
    assert np.all(output[:a.size] == a)  # Check repeated elements match the original array

@given(st.lists(st.integers(min_value=1, max_value=10), min_size=1).map(tuple))
def test_total_elements_property(new_shape):
    a = np.arange(np.prod(new_shape))
    output = resize(a, new_shape)
    assert output.size == np.prod(new_shape)

# End program