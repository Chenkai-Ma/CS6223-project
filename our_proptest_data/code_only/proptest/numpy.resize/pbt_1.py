from hypothesis import given, strategies as st
import numpy as np
from numpy import resize

@given(st.lists(st.integers(), min_size=1).map(np.array), 
       st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_output_shape_property(arr, new_shape):
    result = resize(arr, new_shape)
    assert result.shape == tuple(new_shape)
# End program

@given(st.lists(st.integers(), min_size=1).map(np.array))
def test_empty_input_property(arr):
    result = resize(arr, (0,))
    assert result.size == 0
    assert result.shape == (0,)
# End program

@given(st.lists(st.integers(), min_size=1).map(np.array), 
       st.lists(st.integers(max_value=-1), min_size=1))
def test_negative_dimension_property(arr, negative_shape):
    with pytest.raises(ValueError):
        resize(arr, negative_shape)
# End program

@given(st.lists(st.integers(), min_size=1).map(np.array), 
       st.lists(st.integers(), min_size=1).map(np.array))
def test_repeated_elements_property(arr, new_shape):
    result = resize(arr, new_shape)
    expected_size = np.prod(new_shape)
    assert len(result) == expected_size
# End program

@given(st.lists(st.integers(), min_size=1).map(np.array), 
       st.lists(st.integers(min_value=1, max_value=100), min_size=1))
def test_total_elements_property(arr, new_shape):
    result = resize(arr, new_shape)
    assert result.size == np.prod(new_shape)
# End program