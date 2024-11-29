from hypothesis import given, strategies as st
import decimal
import math

@given(st.integers())
def test_output_instance_of_Decimal_property(f):
    result = decimal.Decimal.from_float(f)
    assert isinstance(result, decimal.Decimal)

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_represents_finite_float_property(f):
    if not (math.isinf(f) or math.isnan(f)):
        result = decimal.Decimal.from_float(f)
        assert result == decimal.Decimal(f)

@given(st.floats())
def test_sign_of_output_property(f):
    result = decimal.Decimal.from_float(f)
    if f >= 0:
        assert result.is_signed() == False
    else:
        assert result.is_signed() == True

@given(st.one_of(st.integers(), st.floats()))
def test_type_error_on_invalid_input_property(f):
    if not isinstance(f, (int, float)):
        with pytest.raises(TypeError):
            decimal.Decimal.from_float(f)

@given(st.sampled_from([float('inf'), float('-inf'), float('nan')]))
def test_special_float_inputs_property(f):
    result = decimal.Decimal.from_float(f)
    assert result == repr(f)
# End program