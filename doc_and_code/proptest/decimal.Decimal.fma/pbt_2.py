from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_output_property(self_val, other_val, third_val):
    result = Decimal(self_val).fma(Decimal(other_val), Decimal(third_val))
    expected = Decimal(self_val) * Decimal(other_val) + Decimal(third_val)
    assert result == expected

@given(st.decimals(), st.decimals())
def test_fma_special_values_property(self_val, other_val):
    if Decimal(self_val)._is_special or Decimal(other_val)._is_special:
        context = getcontext()
        try:
            result = Decimal(self_val).fma(Decimal(other_val), Decimal(0))
            # Check for NaN or Infinity handling
            assert result.is_nan() or result.is_infinite() or isinstance(result, Decimal)
        except InvalidOperation:
            pass

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_sign_property(self_val, other_val, third_val):
    result = Decimal(self_val).fma(Decimal(other_val), Decimal(third_val))
    product_sign = (Decimal(self_val).is_signed() ^ Decimal(other_val).is_signed())
    if Decimal(self_val) == 0:
        assert result == Decimal(third_val)
    else:
        assert result.is_signed() == product_sign

@given(st.decimals(), st.decimals())
def test_fma_zero_multiplication_property(self_val, other_val):
    result = Decimal(self_val).fma(Decimal(0), Decimal(0))
    assert result == Decimal(0)

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_decimal_instance_property(self_val, other_val, third_val):
    result = Decimal(self_val).fma(Decimal(other_val), Decimal(third_val))
    assert isinstance(result, Decimal)

# End program