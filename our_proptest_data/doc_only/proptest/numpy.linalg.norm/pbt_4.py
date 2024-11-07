from hypothesis import given, strategies as st
import numpy as np
from numpy import linalg as LA

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_vector_non_negativity_property(data):
    norm_value = LA.norm(data)
    assert norm_value >= 0
    if all(x == 0 for x in data):
        assert norm_value == 0

@given(st.lists(st.lists(st.floats(), min_size=1), min_size=1, max_size=100))
def test_matrix_non_negativity_property(data):
    norm_value = LA.norm(data)
    assert norm_value >= 0
    if all(all(x == 0 for x in row) for row in data):
        assert norm_value == 0

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_frobenius_equals_flattened_2norm_property(data):
    matrix = np.array(data).reshape(-1, 1)  # Reshape to 2-D for consistency
    frobenius_norm = LA.norm(matrix, 'fro')
    flattened_2norm = LA.norm(matrix.ravel())
    assert np.isclose(frobenius_norm, flattened_2norm)

@given(st.lists(st.floats(), min_size=1, max_size=1000), st.floats(allow_nan=False, allow_infinity=False))
def test_scaling_property(data, scalar):
    scaled_data = [scalar * x for x in data]
    assert np.isclose(LA.norm(scaled_data), abs(scalar) * LA.norm(data))

@given(st.lists(st.lists(st.floats(), min_size=1), min_size=1, max_size=100))
def test_axis_norms_property(data):
    matrix = np.array(data)
    row_norms = LA.norm(matrix, axis=1)
    col_norm = LA.norm(matrix, axis=0)
    total_norm = LA.norm(matrix)
    assert np.isclose(total_norm, np.sqrt(np.sum(row_norms**2)))  # Norm consistency across axes

# End program