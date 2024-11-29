from hypothesis import given, strategies as st
import numpy as np
from numpy import linalg as LA

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_zero_vector_norm_property(vec):
    zero_vector = np.zeros(len(vec))
    assert LA.norm(zero_vector) == 0.0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_non_negative_norm_property(vec):
    norm_value = LA.norm(vec)
    assert norm_value >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_ordered_norms_property(vec):
    norm_1 = LA.norm(vec, ord=1)
    norm_2 = LA.norm(vec, ord=2)
    norm_inf = LA.norm(vec, ord=np.inf)
    assert norm_1 <= norm_2 <= norm_inf

@given(st.matrices(elements=st.floats(allow_nan=False, allow_infinity=False), min_size=2, max_size=5))
def test_frobenius_norm_property(mat):
    frobenius_norm = LA.norm(mat, ord='fro')
    singular_value_norm = LA.norm(mat, ord=2)
    assert np.isclose(frobenius_norm, singular_value_norm)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_keepdims_shape_property(vec):
    norm_value = LA.norm(vec, keepdims=True)
    assert norm_value.shape == (1,)
# End program