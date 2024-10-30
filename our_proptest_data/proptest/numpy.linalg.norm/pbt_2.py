from hypothesis import given, strategies as st
import numpy as np
from numpy import linalg as LA

@given(st.lists(st.floats(), min_size=1, max_size=1000))  # Generate non-empty lists of floats
def test_vector_norm_non_negative_property(data):
    norm_value = LA.norm(data)
    assert norm_value >= 0
    if all(x == 0 for x in data):
        assert norm_value == 0  # Only zero vector has zero norm

@given(st.lists(st.lists(st.floats(), min_size=1, max_size=10), min_size=1, max_size=10))  # Generate non-empty 2D lists of floats
def test_matrix_norm_non_negative_property(data):
    norm_value = LA.norm(data)
    assert norm_value >= 0
    if all(all(x == 0 for x in row) for row in data):
        assert norm_value == 0  # Only zero matrix has zero norm

@given(st.lists(st.floats(), min_size=1, max_size=1000))  # Generate non-empty lists of floats
def test_frobenius_and_flattened_2norm_property(data):
    if len(data) > 1:  # Ensure we have at least 2 elements for a matrix
        matrix = np.array(data).reshape(-1, 2)  # Reshape into a 2D array
        frobenius_norm = LA.norm(matrix, 'fro')
        flattened_2norm = LA.norm(matrix.ravel())
        assert np.isclose(frobenius_norm, flattened_2norm)

@given(st.floats(min_value=-1000, max_value=1000), st.lists(st.floats(), min_size=1, max_size=1000))  # Generate a scalar and a list
def test_norm_scaling_property(scalar, data):
    scaled_data = [x * scalar for x in data]
    norm_value = LA.norm(data)
    scaled_norm_value = LA.norm(scaled_data)
    assert np.isclose(scaled_norm_value, abs(scalar) * norm_value)

@given(st.lists(st.lists(st.floats(), min_size=1, max_size=10), min_size=1, max_size=10))  # Generate non-empty 2D lists of floats
def test_axis_norms_consistency_property(data):
    if len(data) > 1 and len(data[0]) > 1:  # Ensure we have at least a 2D matrix
        matrix = np.array(data)
        overall_norm = LA.norm(matrix)
        row_norms = LA.norm(matrix, axis=1)
        assert np.isclose(overall_norm, np.sum(row_norms))  # This may vary based on norm type, but illustrates the idea
# End program