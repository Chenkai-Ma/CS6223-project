from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_output_equals_product_plus_third_property(self, other, third):
    result = self.fma(other, third)
    assert result == self * other + third
# End program

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_output_type_property(self, other, third):
    result = self.fma(other, third)
    assert isinstance(result, Decimal)
# End program

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_zero_other_property(self, self, third):
    result = self.fma(0, third)
    assert result == self + third
# End program

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_zero_third_property(self, self, other):
    result = self.fma(other, 0)
    assert result == self * other
# End program

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_commutative_property(self, self, other):
    third = Decimal('1')  # Using a constant third for clarity
    result1 = self.fma(other, third)
    result2 = self.fma(third, other)
    assert result1 == result2
# End program

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_no_rounding_property(self, self, other, third):
    context = Decimal.getcontext()
    original_rounding = context.rounding
    context.rounding = 'ROUND_DOWN'  # Change rounding for the test
    result_with_rounding = self.fma(other, third)
    context.rounding = original_rounding  # Reset to original
    assert result_with_rounding == self * other + third
# End program