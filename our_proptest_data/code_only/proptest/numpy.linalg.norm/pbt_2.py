from hypothesis import given, strategies as st
import numpy as np
from numpy.linalg import norm

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_vector_norm_non_negative_property(vec):
    result = norm(vec, ord=2)
    assert result >= 0
    assert (result == 0) == all(v == 0 for v in vec)

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, max_size=100, max_len=100))
def test_frobenius_norm_property(mat):
    mat_array = np.array(mat)
    result = norm(mat_array, ord='fro')
    assert result >= 0
    expected = np.sqrt(np.sum(np.abs(mat_array)**2))
    assert np.isclose(result, expected)

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, max_size=100, max_len=100))
def test_inf_norm_property(mat):
    mat_array = np.array(mat)
    result = norm(mat_array, ord=np.inf)
    assert result >= 0
    expected = np.max(np.sum(np.abs(mat_array), axis=1))
    assert np.isclose(result, expected)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_zero_norm_property(vec):
    result = norm(vec, ord=0)
    count_non_zero = sum(v != 0 for v in vec)
    assert result == count_non_zero

@given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False)), min_size=1, max_size=100, max_len=100))
def test_unitary_invariance_property(mat):
    mat_array = np.array(mat)
    # Generate a random unitary matrix
    u, _, _ = np.linalg.svd(np.random.rand(2, 2))
    transformed = u @ mat_array @ u.T
    assert np.isclose(norm(mat_array), norm(transformed))
# End program