from hypothesis import given, strategies as st
import numpy as np
import sys

@given(st.lists(st.integers(), min_size=1), st.lists(st.integers(min_value=0), max_size=5))
def test_output_shape_property(input_list, new_shape):
    a = np.array(input_list)
    resized = np.resize(a, new_shape)
    assert resized.shape == tuple(new_shape)
# End program

@given(st.lists(st.integers()))
def test_empty_input_property(input_list):
    a = np.array(input_list)
    resized = np.resize(a, (0,))
    assert resized.size == 0
    assert resized.shape == (0,)
# End program

@given(st.lists(st.integers()), st.lists(st.integers(min_value=-1, max_value=5), min_size=1))
def test_negative_dimension_property(input_list, new_shape):
    a = np.array(input_list)
    try:
        np.resize(a, new_shape)
        assert all(dim >= 0 for dim in new_shape)
    except ValueError:
        assert any(dim < 0 for dim in new_shape)
# End program

@given(st.lists(st.integers()), st.lists(st.integers(min_value=1, max_value=5)))
def test_element_repetition_property(input_list, new_shape):
    a = np.array(input_list)
    resized = np.resize(a, new_shape)
    expected_size = np.prod(new_shape)
    original_size = a.size
    repeats = -(-expected_size // original_size) if original_size > 0 else 0
    expected_elements = np.concatenate((a,) * repeats)[:expected_size]
    assert np.array_equal(resized, expected_elements)
# End program

@given(st.lists(st.integers()), st.lists(st.integers(min_value=1, max_value=sys.maxsize), min_size=1))
def test_total_elements_property(input_list, new_shape):
    a = np.array(input_list)
    resized = np.resize(a, new_shape)
    assert resized.size == np.prod(new_shape)
# End program