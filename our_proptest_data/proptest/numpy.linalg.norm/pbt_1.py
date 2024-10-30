from hypothesis import given, strategies as st
import numpy as np
from numpy import linalg as LA

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_vector_non_negativity_property(data):
    vector = np.array(data)
    norm_value = LA.norm(vector)
    assert norm_value >= 0
    if np.all(vector == 0):
        assert norm_value == 0

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, min_size=1))
def test_matrix_non_negativity_property(data):
    matrix = np.array(data)
    norm_value = LA.norm(matrix)
    assert norm_value >= 0
    if np.all(matrix == 0):
        assert norm_value == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_frobenius_and_flattened_2norm_property(data):
    matrix = np.array(data).reshape(-1, len(data)//2) if len(data) % 2 == 0 else np.array(data).reshape(-1, len(data)//3)
    frobenius_norm = LA.norm(matrix, 'fro')
    flattened_2norm = LA.norm(matrix.ravel())
    assert np.isclose(frobenius_norm, flattened_2norm)

@given(st.floats(min_value=-1e6, max_value=1e6), st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_scalar_multiplication_property(scalar, data):
    vector = np.array(data)
    norm_original = LA.norm(vector)
    norm_scaled = LA.norm(scalar * vector)
    assert np.isclose(norm_scaled, abs(scalar) * norm_original)

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, min_size=1))
def test_axis_norm_consistency_property(data):
    matrix = np.array(data)
    axis_0_norm = LA.norm(matrix, axis=0)
    axis_1_norm = LA.norm(matrix, axis=1)
    total_norm = LA.norm(matrix)
    assert np.isclose(np.sum(axis_0_norm), total_norm) or np.isclose(np.sum(axis_1_norm), total_norm)

# End program