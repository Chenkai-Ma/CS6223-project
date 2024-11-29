from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_correctness_property(x, y, z):
    """Property: The result of fma(x, y, z) should equal x * y + z for finite inputs."""
    if x.is_finite() and y.is_finite():
        assert x.fma(y, z) == x * y + z

@given(st.decimals())
def test_fma_signaling_nan_property(x):
    """Property: If x is a signaling NaN, fma(x, y, z) should raise an InvalidOperation error."""
    if x.is_snan():
        with pytest.raises(InvalidOperation):
            x.fma(Decimal(1), Decimal(1))

@given(st.decimals())
def test_fma_quiet_nan_property(x):
    """Property: If x is a quiet NaN, fma(x, y, z) should return y + z."""
    if x.is_nan():
        result = x.fma(Decimal(1), Decimal(1))
        assert result == Decimal(1) + Decimal(1)

@given(st.decimals(), st.decimals())
def test_fma_infinity_property(x, y):
    """Property: If x or y is infinity, the product should be calculated correctly."""
    if x.is_infinite() or y.is_infinite():
        if x.is_infinite() and y.is_zero():
            with pytest.raises(InvalidOperation):
                x.fma(y, Decimal(1))
        else:
            result = x.fma(y, Decimal(1))
            assert result.is_infinite()

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_sign_property(x, y, z):
    """Property: The output of fma(x, y, z) should maintain the sign of x * y."""
    if x.is_finite() and y.is_finite() and x != 0 and y != 0:
        product_sign = (x.sign() * y.sign())
        result = x.fma(y, z)
        assert result.sign() == product_sign

# End program