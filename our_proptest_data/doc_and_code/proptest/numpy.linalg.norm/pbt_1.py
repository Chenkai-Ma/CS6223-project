from hypothesis import given, strategies as st
import numpy as np

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_norm_of_zero_vector_property(vec):
    zero_vector = np.zeros_like(vec)
    assert np.linalg.norm(zero_vector) == 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_non_negative_norm_property(vec):
    norm_value = np.linalg.norm(vec)
    assert norm_value >= 0

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_ordered_norms_property(vec):
    norm_1 = np.linalg.norm(vec, ord=1)
    norm_2 = np.linalg.norm(vec, ord=2)
    norm_inf = np.linalg.norm(vec, ord=np.inf)
    assert norm_1 <= norm_2 <= norm_inf

@given(st.matrices(elements=st.floats(allow_nan=False, allow_infinity=False), min_rows=1, min_cols=1))
def test_frobenius_and_singular_property(mat):
    frobenius_norm = np.linalg.norm(mat, ord='fro')
    singular_norm = np.linalg.norm(mat, ord=2)
    assert np.isclose(frobenius_norm, singular_norm, rtol=1e-5)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_keepdims_property(vec):
    norm_value_keepdims = np.linalg.norm(vec, keepdims=True)
    assert norm_value_keepdims.shape == (1,)
# End program