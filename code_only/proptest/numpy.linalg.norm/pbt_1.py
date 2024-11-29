from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.floats(), max_size=1000))  # Testing vectors with float values
def test_norm_vector_non_negative_property(vector):
    result = np.linalg.norm(vector, ord=2)
    assert result >= 0
    if all(v == 0 for v in vector):
        assert result == 0

@given(st.lists(st.lists(st.floats()), max_size=100, min_size=10, max_size=100))  # Testing matrices with float values
def test_norm_frobenius_non_negative_property(matrix):
    result = np.linalg.norm(matrix, ord='fro')
    assert result >= 0

@given(st.lists(st.lists(st.floats()), max_size=100, min_size=10, max_size=100))  # Testing matrices with float values
def test_norm_inf_matrix_property(matrix):
    result = np.linalg.norm(matrix, ord=np.inf)
    assert result >= 0

@given(st.lists(st.floats(), max_size=1000))  # Testing vectors with float values
def test_norm_zero_count_property(vector):
    result = np.linalg.norm(vector, ord=0)
    assert result == sum(1 for v in vector if v != 0)

@given(st.lists(st.lists(st.floats()), max_size=100, min_size=10, max_size=100))  # Testing matrices with float values
def test_norm_unitary_invariance_property(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return  # Skip empty matrices
    unitary_matrix = np.linalg.qr(np.random.rand(len(matrix), len(matrix[0])))[0]  # Generate a random unitary matrix
    transformed_matrix = unitary_matrix @ matrix
    original_norm = np.linalg.norm(matrix, ord=2)
    transformed_norm = np.linalg.norm(transformed_matrix, ord=2)
    assert np.isclose(original_norm, transformed_norm)

# End program