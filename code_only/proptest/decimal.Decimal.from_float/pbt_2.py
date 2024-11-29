from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.integers())
def test_output_is_instance_of_Decimal_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_equals_decimal_of_float_property(f):
    result = Decimal.from_float(f)
    assert result == Decimal(f)

@given(st.floats())
def test_sign_of_output_matches_input_property(f):
    result = Decimal.from_float(f)
    if f >= 0:
        assert result.is_signed() == 0  # Positive sign
    else:
        assert result.is_signed() == 1  # Negative sign

@given(st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False)))
def test_type_error_on_invalid_input_property(f):
    if isinstance(f, (int, float)):
        try:
            Decimal.from_float(f)
        except TypeError:
            assert False, "TypeError should not be raised for valid inputs"
    else:
        try:
            Decimal.from_float("invalid")
        except TypeError:
            pass  # Expected behavior

@given(st.one_of(st.floats(allow_nan=True, allow_infinity=True), st.just(float('inf')), st.just(float('-inf')), st.just(float('nan'))))
def test_special_float_output_property(f):
    result = Decimal.from_float(f)
    if math.isinf(f):
        assert result == Decimal(repr(f))
    elif math.isnan(f):
        assert result == Decimal(repr(f))

# End program