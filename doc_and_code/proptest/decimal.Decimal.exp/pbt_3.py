from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.floats(allow_nan=False, allow_infinity=False))  # Generate finite floats
def test_decimal_Decimal_exp_positive_output_property(x):
    result = Decimal(x).exp()
    assert result > 0  # Exponential function should always return a positive value

@given(st.just(0.0))  # Test only the input 0
def test_decimal_Decimal_exp_zero_property():
    result = Decimal(0).exp()
    assert result == Decimal(1)  # Exponential function should return 1 for input 0

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e100, max_value=0))  # Generate negative floats
def test_decimal_Decimal_exp_negative_infinity_property(x):
    result = Decimal(x).exp()
    assert result < 1  # Exponential function should approach 0 as input approaches negative infinity

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=0, max_value=1e100))  # Generate positive floats
def test_decimal_Decimal_exp_positive_infinity_property(x):
    result = Decimal(x).exp()
    assert result > 1  # Exponential function should approach infinity as input approaches positive infinity

@given(st.floats())
def test_decimal_Decimal_exp_rounding_property(x):
    result = Decimal(x).exp()
    # Check if the result is correctly rounded using ROUND_HALF_EVEN
    context = getcontext()
    context.rounding = 'ROUND_HALF_EVEN'
    expected = result.quantize(Decimal('1.0'))  # Example quantization for checking rounding
    assert result == expected  # Ensure the result is correctly rounded
# End program