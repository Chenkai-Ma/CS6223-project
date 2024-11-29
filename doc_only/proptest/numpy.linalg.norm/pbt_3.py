from hypothesis import given, strategies as st
import numpy as np
from numpy import linalg as LA

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_non_negative_norm_property(vector):
    norm_value = LA.norm(vector)
    assert norm_value >= 0
    if all(v == 0 for v in vector):
        assert norm_value == 0

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, max_size=5))
def test_zero_matrix_norm_property(matrix):
    matrix_np = np.array(matrix)
    norm_value = LA.norm(matrix_np)
    assert norm_value >= 0
    if np.all(matrix_np == 0):
        assert norm_value == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_frobenius_equals_2norm_property(vector):
    matrix_np = np.array(vector).reshape(-1, 1)  # Reshape to 2D
    frobenius_norm = LA.norm(matrix_np, 'fro')
    vector_norm = LA.norm(matrix_np.ravel())
    assert np.isclose(frobenius_norm, vector_norm)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1), st.floats())
def test_scalar_multiplication_property(vector, scalar):
    norm_value = LA.norm(vector)
    scaled_vector = [v * scalar for v in vector]
    scaled_norm_value = LA.norm(scaled_vector)
    assert np.isclose(scaled_norm_value, abs(scalar) * norm_value)

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, max_size=5))
def test_axis_consistency_property(matrix):
    matrix_np = np.array(matrix)
    norm_over_all = LA.norm(matrix_np)
    norm_along_axis0 = LA.norm(matrix_np, axis=0)
    norm_along_axis1 = LA.norm(matrix_np, axis=1)
    
    # Check if the sum of norms along axis 0 gives the overall norm (1-D case)
    assert np.isclose(norm_over_all, np.sum(norm_along_axis0))
    # Check if the sum of norms along axis 1 gives the overall norm (1-D case)
    assert np.isclose(norm_over_all, np.sum(norm_along_axis1))

# End program