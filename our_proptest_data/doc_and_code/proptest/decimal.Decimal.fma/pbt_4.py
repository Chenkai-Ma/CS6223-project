from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_output_equals_product_plus_third_property(a, b, c):
    result = Decimal(a).fma(Decimal(b), Decimal(c))
    expected = Decimal(a) * Decimal(b) + Decimal(c)
    assert result == expected

@given(st.decimals(), st.decimals())
def test_fma_special_values_property(a, b):
    if Decimal(a)._is_special or Decimal(b)._is_special:
        result = Decimal(a).fma(Decimal(b), Decimal(0))
        if Decimal(a)._exp == 'N' or Decimal(b)._exp == 'N':
            # Expecting an error for NaN
            try:
                Decimal(a).fma(Decimal(b), Decimal(0))
                assert False, "Expected InvalidOperation for NaN"
            except InvalidOperation:
                pass
        elif Decimal(a)._exp == 'F' or Decimal(b)._exp == 'F':
            # Expecting infinity handling
            assert isinstance(result, Decimal)  # Result should still be a Decimal
        else:
            assert True  # Normal case

@given(st.decimals(), st.decimals())
def test_fma_sign_property(a, b):
    if Decimal(a) != 0 and Decimal(b) != 0:
        result = Decimal(a).fma(Decimal(b), Decimal(0))
        assert (result.sign() == (Decimal(a).sign() * Decimal(b).sign()))

@given(st.decimals(), st.decimals())
def test_fma_zero_multiplication_property(a, b):
    result = Decimal(a).fma(0, Decimal(b))
    assert result == Decimal(b)

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_result_is_decimal_property(a, b, c):
    result = Decimal(a).fma(Decimal(b), Decimal(c))
    assert isinstance(result, Decimal)
# End program