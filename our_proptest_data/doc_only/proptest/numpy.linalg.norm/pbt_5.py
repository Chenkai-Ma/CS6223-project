from hypothesis import given, strategies as st
import numpy as np
from numpy import linalg as LA

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_non_negative_norm_of_vector_property(vec):
    norm_value = LA.norm(vec)
    assert norm_value >= 0
    if all(v == 0 for v in vec):
        assert norm_value == 0

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, min_size=1))
def test_non_negative_norm_of_matrix_property(mat):
    mat_array = np.array(mat)
    norm_value = LA.norm(mat_array)
    assert norm_value >= 0
    if np.all(mat_array == 0):
        assert norm_value == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_frobenius_norm_equals_2norm_of_flattened_matrix_property(vec):
    mat = np.array(vec).reshape(-1, 1)  # Reshape to 2-D
    frobenius_norm = LA.norm(mat, 'fro')
    flattened_2norm = LA.norm(mat.ravel())
    assert np.isclose(frobenius_norm, flattened_2norm)

@given(st.floats(allow_nan=False, allow_infinity=False), st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_scalar_multiplication_property(scalar, vec):
    scaled_vec = [scalar * v for v in vec]
    norm_value = LA.norm(vec)
    scaled_norm_value = LA.norm(scaled_vec)
    assert np.isclose(scaled_norm_value, abs(scalar) * norm_value)

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1))
def test_consistent_norm_across_axes_property(mat):
    mat_array = np.array(mat)
    if mat_array.ndim != 2:
        return  # Skip if not a 2-D array
    overall_norm = LA.norm(mat_array)
    row_norms = LA.norm(mat_array, axis=1)
    col_norms = LA.norm(mat_array, axis=0)

    assert np.isclose(overall_norm, np.sqrt(np.sum(row_norms**2)))
    assert np.isclose(overall_norm, np.sqrt(np.sum(col_norms**2)))

# End program