from hypothesis import given, strategies as st
import numpy as np
from numpy import linalg as LA

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_norm_of_zero_vector_property(x):
    """The norm of a zero vector should always be zero."""
    zero_vector = np.zeros_like(x)
    assert np.isclose(LA.norm(zero_vector), 0.0)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_norm_non_negative_property(x):
    """The norm should be non-negative for any input vector or matrix."""
    vector = np.array(x)
    assert LA.norm(vector) >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000))
def test_norms_order_property(x):
    """For any vector, the norm with ord=1 should be <= ord=2 <= ord=np.inf."""
    vector = np.array(x)
    norm_1 = LA.norm(vector, ord=1)
    norm_2 = LA.norm(vector, ord=2)
    norm_inf = LA.norm(vector, ord=np.inf)
    assert norm_1 <= norm_2 <= norm_inf

@given(st.matrices(st.floats(allow_nan=False, allow_infinity=False), min_rows=1, min_cols=1, max_rows=10, max_cols=10))
def test_frobenius_and_singular_norm_property(matrix):
    """The Frobenius norm should equal the 2-norm calculated from singular values."""
    mat = np.array(matrix)
    frobenius_norm = LA.norm(mat, ord='fro')
    singular_value_norm = LA.norm(mat, ord=2)
    assert np.isclose(frobenius_norm, singular_value_norm)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1, max_size=1000),
           st.booleans())
def test_keepdims_shape_property(x, keepdims):
    """The result should maintain the same shape as the input when keepdims=True."""
    vector = np.array(x)
    norm_result = LA.norm(vector, keepdims=keepdims)
    expected_shape = vector.shape if keepdims else ()
    assert norm_result.shape == expected_shape

# End program