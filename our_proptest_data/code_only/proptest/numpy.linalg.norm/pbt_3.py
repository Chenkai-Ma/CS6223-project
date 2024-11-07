from hypothesis import given, strategies as st
import numpy as np
from numpy.linalg import norm

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_vector_norm_non_negative_property(vec):
    result = norm(vec, ord=2)
    assert result >= 0
    assert (result == 0) == all(v == 0 for v in vec)

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, max_size=100, max_depth=2))
def test_frobenius_norm_non_negative_property(mat):
    result = norm(mat, ord='fro')
    assert result >= 0

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, max_size=100, max_depth=2))
def test_inf_norm_maximum_row_sum_property(mat):
    result = norm(mat, ord=np.inf)
    max_row_sum = max(np.sum(np.abs(row)) for row in mat)
    assert result == max_row_sum

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_zero_norm_count_non_zero_elements_property(vec):
    result = norm(vec, ord=0)
    assert result == sum(1 for v in vec if v != 0)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_invariance_under_unitary_property(vec):
    unitary_matrix = np.eye(len(vec))  # Identity matrix as a trivial unitary transformation
    original_norm = norm(vec)
    transformed_norm = norm(np.dot(unitary_matrix, vec))
    assert original_norm == transformed_norm
# End program