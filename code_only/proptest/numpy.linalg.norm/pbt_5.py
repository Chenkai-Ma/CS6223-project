from hypothesis import given, strategies as st
import numpy as np
from numpy.linalg import norm

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_vector_norm_non_negative_property(vec):
    result = norm(vec, ord=2)
    assert result >= 0
    if all(v == 0 for v in vec):
        assert result == 0

@given(st.matrices(st.floats(), min_rows=1, min_cols=1, max_rows=100, max_cols=100))
def test_matrix_frobenius_norm_property(mat):
    result = norm(mat, ord='fro')
    assert result >= 0
    expected = np.sqrt(np.sum(np.square(mat)))
    assert np.isclose(result, expected)

@given(st.matrices(st.floats(), min_rows=1, min_cols=1, max_rows=100, max_cols=100))
def test_matrix_inf_norm_property(mat):
    result = norm(mat, ord=np.inf)
    assert result >= 0
    expected = np.max(np.sum(np.abs(mat), axis=1))
    assert np.isclose(result, expected)

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_vector_zero_norm_property(vec):
    result = norm(vec, ord=0)
    assert isinstance(result, int)
    assert result >= 0
    assert result == sum(1 for v in vec if v != 0)

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_unitary_transform_invariance_property(vec):
    unitary_matrix = np.random.randn(len(vec), len(vec))
    unitary_matrix, _ = np.linalg.qr(unitary_matrix)  # Ensure it's unitary
    transformed_vec = unitary_matrix @ vec
    result_original = norm(vec, ord=2)
    result_transformed = norm(transformed_vec, ord=2)
    assert np.isclose(result_original, result_transformed)
# End program