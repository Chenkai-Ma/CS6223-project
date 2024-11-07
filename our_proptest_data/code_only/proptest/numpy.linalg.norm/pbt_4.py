from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_vector_norm_non_negative_property(vector):
    norm_value = np.linalg.norm(vector, ord=2)
    assert norm_value >= 0
    assert (norm_value == 0) == all(v == 0 for v in vector)

@given(st.lists(st.lists(st.floats()), min_size=1, max_size=100, max_length=100), 
               st.booleans())
def test_frobenius_norm_non_negative_property(matrix, keepdims):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return  # Skip empty matrices
    norm_value = np.linalg.norm(matrix, ord='fro', keepdims=keepdims)
    assert norm_value >= 0

@given(st.lists(st.lists(st.floats()), min_size=1, max_size=100, max_length=100), 
               st.booleans())
def test_matrix_inf_norm_non_negative_property(matrix, keepdims):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return  # Skip empty matrices
    norm_value = np.linalg.norm(matrix, ord=np.inf, keepdims=keepdims)
    assert norm_value >= 0

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_zero_norm_non_negative_integer_property(vector):
    norm_value = np.linalg.norm(vector, ord=0)
    assert isinstance(norm_value, int)
    assert norm_value >= 0

@given(st.lists(st.lists(st.floats(), min_size=1, max_size=100, max_length=100)),
               st.lists(st.lists(st.floats()), min_size=1, max_size=100, max_length=100)))
def test_unitary_invariance_property(matrix1, matrix2):
    if len(matrix1) == 0 or len(matrix1[0]) == 0 or len(matrix2) == 0 or len(matrix2[0]) == 0:
        return  # Skip empty matrices
    norm_before = np.linalg.norm(matrix1)
    norm_after = np.linalg.norm(np.dot(matrix1, matrix2))
    assert norm_before == norm_after

# End program