from hypothesis import given, strategies as st
import decimal
import math

@given(st.integers())
def test_decimal_Decimal_from_float_integer_property(i):
    result = decimal.Decimal.from_float(i)
    assert isinstance(result, decimal.Decimal)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_from_float_finite_float_property(f):
    result = decimal.Decimal.from_float(f)
    assert result == decimal.Decimal(f)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_from_float_sign_property(f):
    result = decimal.Decimal.from_float(f)
    if f >= 0:
        assert result >= 0
    else:
        assert result < 0

@given(st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False)))
def test_decimal_Decimal_from_float_type_error_property(x):
    if isinstance(x, float) and (math.isinf(x) or math.isnan(x)):
        result = decimal.Decimal.from_float(x)
        assert isinstance(result, decimal.Decimal)  # Should return Decimal for special floats
    else:
        with st.raises(TypeError):
            decimal.Decimal.from_float("string")  # Testing invalid input type

@given(st.one_of(st.floats(allow_nan=True, allow_infinity=True)))
def test_decimal_Decimal_from_float_special_float_property(f):
    result = decimal.Decimal.from_float(f)
    if math.isinf(f):
        assert result == decimal.Decimal(repr(f))
    elif math.isnan(f):
        assert result == decimal.Decimal(repr(f))

# End program