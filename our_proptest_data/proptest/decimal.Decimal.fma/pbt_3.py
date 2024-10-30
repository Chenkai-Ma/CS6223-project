from hypothesis import given, strategies as st
from decimal import Decimal, getcontext

# Set a high precision context to handle large inputs and avoid overflow
getcontext().prec = 50

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_output_equivalence_property(x, y, z):
    """The output should be equal to self * other + third."""
    result = Decimal(x).fma(Decimal(y), Decimal(z))
    expected = Decimal(x) * Decimal(y) + Decimal(z)
    assert result == expected

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_output_type_property(x, y, z):
    """The output should be a Decimal type."""
    result = Decimal(x).fma(Decimal(y), Decimal(z))
    assert isinstance(result, Decimal)

@given(st.decimals(), st.decimals())
def test_fma_zero_other_property(x, z):
    """If other is zero, the output should equal self + third."""
    result = Decimal(x).fma(Decimal(0), Decimal(z))
    expected = Decimal(x) + Decimal(z)
    assert result == expected

@given(st.decimals(), st.decimals())
def test_fma_zero_third_property(x, y):
    """If third is zero, the output should equal self * other."""
    result = Decimal(x).fma(Decimal(y), Decimal(0))
    expected = Decimal(x) * Decimal(y)
    assert result == expected

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_commutative_property(y, z, x):
    """The output should be consistent with the commutative property of addition."""
    result1 = Decimal(x).fma(Decimal(y), Decimal(z))
    result2 = Decimal(x).fma(Decimal(z), Decimal(y))
    assert result1 == result2

# End program