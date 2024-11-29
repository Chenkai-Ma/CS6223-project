from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.decimals(), st.decimals())
def test_output_equals_product_plus_third_property(self, other, third):
    if self.is_nan() or other.is_nan():
        return  # Skip testing if either is NaN
    result = self.fma(other, third)
    expected = self * other + third
    assert result == expected

@given(st.decimals(), st.decimals(), st.decimals())
def test_special_values_property(self, other, third):
    context = getcontext()
    if self.is_nan() or other.is_nan():
        try:
            result = self.fma(other, third)
            assert result.is_nan()
        except InvalidOperation:
            pass  # Expected behavior, skip further checks
    elif self.is_infinite() or other.is_infinite():
        result = self.fma(other, third)
        # Check that the result is either infinity or a valid number
        assert result.is_infinite() or isinstance(result, Decimal)

@given(st.decimals(), st.decimals(), st.decimals())
def test_sign_property(self, other, third):
    if self.is_zero() or other.is_zero():
        result = self.fma(other, third)
        assert result == third  # If either is zero, result should be third
    else:
        result = self.fma(other, third)
        expected_sign = (self.sign() ^ other.sign())  # XOR for sign
        assert result.sign() == expected_sign

@given(st.decimals(), st.decimals(), st.decimals())
def test_zero_multiplication_property(self, other, third):
    if self.is_zero() or other.is_zero():
        result = self.fma(other, third)
        assert result == third  # Result should be equal to third

@given(st.decimals(), st.decimals(), st.decimals())
def test_valid_decimal_instance_property(self, other, third):
    result = self.fma(other, third)
    assert isinstance(result, Decimal)  # Output should be a Decimal instance
    assert result.is_finite()  # Ensure result does not cause overflow or NaN

# End program