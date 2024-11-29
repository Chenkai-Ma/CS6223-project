from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals())
def test_output_is_valid_decimal_property(decimal_value):
    context = getcontext()
    result = Decimal(decimal_value).shift(Decimal(1), context)
    assert isinstance(result, Decimal)

@given(st.decimals())
def test_shifting_by_zero_returns_same_value_property(decimal_value):
    context = getcontext()
    result = Decimal(decimal_value).shift(Decimal(0), context)
    assert result == Decimal(decimal_value)

@given(st.decimals(), st.integers())
def test_exponent_adjustment_property(decimal_value, shift_amount):
    context = getcontext()
    original_decimal = Decimal(decimal_value)
    result = original_decimal.shift(Decimal(shift_amount), context)
    expected_exponent = original_decimal._exp + int(shift_amount)
    assert result._exp == expected_exponent

@given(st.decimals(), st.integers())
def test_significant_digits_within_precision_property(decimal_value, shift_amount):
    context = getcontext()
    context.prec = 10  # Set precision for testing
    result = Decimal(decimal_value).shift(Decimal(shift_amount), context)
    significant_digits = str(result).replace('.', '').lstrip('0')
    assert len(significant_digits) <= context.prec

@given(st.decimals(), st.integers())
def test_infinity_preserved_property(decimal_value, shift_amount):
    context = getcontext()
    infinite_decimal = Decimal('Infinity')
    result = infinite_decimal.shift(Decimal(shift_amount), context)
    assert result == infinite_decimal
# End program