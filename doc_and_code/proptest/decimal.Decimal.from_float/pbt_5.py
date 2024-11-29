from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_is_instance_of_Decimal_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_represents_nearest_decimal_equivalent_property(f):
    result = Decimal.from_float(f)
    expected = Decimal(str(f))
    assert result == expected

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_special_float_values_property(f):
    if math.isnan(f):
        assert Decimal.from_float(f) == Decimal('NaN')
    elif math.isinf(f):
        assert Decimal.from_float(f) == Decimal('Infinity') if f > 0 else Decimal('-Infinity')

@given(st.integers())
def test_integer_conversion_property(i):
    result = Decimal.from_float(i)
    expected = Decimal(str(abs(i)))
    assert result == expected
    assert result.is_signed() == (i < 0)

@given(st.floats())
def test_sign_of_output_matches_input_property(f):
    result = Decimal.from_float(f)
    assert (result.is_signed() == (f < 0))
# End program