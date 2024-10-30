from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(min_value=-1e+100, max_value=1e+100), 
       st.floats(min_value=-1e+100, max_value=1e+100), 
       st.floats(min_value=-1e+100, max_value=1e+100))
def test_fma_output_equivalence_property(a, b, c):
    result = Decimal(a).fma(Decimal(b), Decimal(c))
    assert result == Decimal(a) * Decimal(b) + Decimal(c)

@given(st.floats(min_value=-1e+100, max_value=1e+100), 
       st.floats(min_value=-1e+100, max_value=1e+100))
def test_fma_output_type_property(a, b):
    result = Decimal(a).fma(Decimal(b), Decimal(0))
    assert isinstance(result, Decimal)

@given(st.floats(min_value=-1e+100, max_value=1e+100))
def test_fma_with_zero_other_property(a):
    result = Decimal(a).fma(0, Decimal(5))
    assert result == Decimal(a) + Decimal(5)

@given(st.floats(min_value=-1e+100, max_value=1e+100))
def test_fma_with_zero_third_property(a):
    result = Decimal(a).fma(Decimal(3), 0)
    assert result == Decimal(a) * Decimal(3)

@given(st.floats(min_value=-1e+100, max_value=1e+100), 
       st.floats(min_value=-1e+100, max_value=1e+100))
def test_fma_commutativity_property(a, b):
    result1 = Decimal(a).fma(Decimal(b), Decimal(5))
    result2 = Decimal(b).fma(Decimal(a), Decimal(5))
    assert result1 == result2

# End program